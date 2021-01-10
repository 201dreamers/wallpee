import random
import os.path

import requests
from fake_useragent import UserAgent, FakeUserAgentError
from bs4 import BeautifulSoup

from misc import (determine_screen_orientation, choose_keyword, monitor,
                  exit_with_message)
from config import UnsplashConfig


class UnsplashProvider:
    """Provider that scrape image from unsplash and save image to file"""

    __slots__ = (
        'images_grid_url', 'screen_orientation', 'path_for_image')

    def __init__(self, path_for_image: str):
        self.path_for_image = path_for_image
        self.screen_orientation = determine_screen_orientation()
        self.images_grid_url = self._create_link_on_images_grid()

    def _create_link_on_images_grid(self):
        """Create link that will point to the page with images grid that
        fits your screen the best
        """
        keyword = choose_keyword()
        order_by = 'order_by=latest'
        orientation = (f'&orientation={self.screen_orientation}'
                       if self.screen_orientation != 'any orientation' else '')
        return (f'{UnsplashConfig.URL}/s/photos/'
                f'{keyword}?{order_by}{orientation}')

    @staticmethod
    def _create_link_for_image_download(image_url, width):
        """Having part of url that points on image, create link that will
        allow to download that image
        """
        return f'{UnsplashConfig.URL}{image_url}/download?force=true&w={width}'

    @staticmethod
    def send_get_request(url) -> requests.Response:
        """Send GET request to url with fake user-agent. Also handle errors"""
        try:
            headers = {
                'User-Agent': UserAgent().chrome
            }
            response = requests.get(
                url, headers=headers,
                timeout=UnsplashConfig.TIMEOUT
            )
            response.raise_for_status()
        except FakeUserAgentError:
            exit_with_message('ERROR: Sorry, some error occured  :(', 1)
        except (requests.exceptions.Timeout, requests.HTTPError):
            exit_with_message(f'ERROR: Can\'t connect to {url}  :(', 1)
        return response

    def _get_image_download_link(self) -> str:
        """Get link that will allow to download image from unsplash.com"""
        # Get html code of page with images grid
        html = self.send_get_request(self.images_grid_url).content
        soup = BeautifulSoup(html, features='lxml')

        # Find exactly images grid on page
        images_grid_dom = soup.find(
            'div', attrs={'data-test': 'search-photos-route'})
        if images_grid_dom is None:
            exit_with_message('ERROR: Can\'t find grid with images  :(', 1)

        # Find all <a> tags that are matching images
        images_tags = images_grid_dom.find_all('a', class_='_2Mc8_')
        if len(images_tags) == 0:
            exit_with_message('ERROR: Can\' find images  :(', 1)

        # Choose random <a> tag and get link on image from it
        image_preview_webelem = random.choice(images_tags)
        image_partial_link = image_preview_webelem.get('href')
        if image_partial_link is None:
            exit_with_message('ERROR: Image has no link  :(', 1)

        # Get closest value from list to screen size
        closest_width = min(
            UnsplashConfig.IMAGE_WIDTHS,
            key=lambda x: abs(x - monitor.width)
        )
        image_download_link = self._create_link_for_image_download(
            image_partial_link, closest_width)

        return image_download_link

    def download_random_image(self) -> str:
        """Download random image from unsplash.com that fits your screen"""
        image_download_link = self._get_image_download_link()
        download_image_response = self.send_get_request(image_download_link)
        # Select the part of url for downloading image that contains file name
        image_name = download_image_response.url.split('&')[-2].split('=')[-1]
        # Create full path to image on the filesystem
        image_path = os.path.join(self.path_for_image, image_name)
        # Write downloaded image to the file by chunks
        with open(image_path, 'wb') as img:
            for chunk in download_image_response.iter_content(chunk_size=1024):
                img.write(chunk)

        return image_path
