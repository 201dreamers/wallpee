import random
import os.path

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from misc import determine_screen_orientation, determine_keyword
from config import UnsplashConfig


class UnsplashParser:

    __slots__ = ('images_grid_url', 'screen_orientation', 'path_for_image')

    def __init__(self, path_for_image):
        self.path_for_image = path_for_image
        self.screen_orientation = determine_screen_orientation()
        self.images_grid_url = self.__join_url_params()

    def __join_url_params(self):
        # Example https://unsplash.com/s/photos/wallpaper?order_by=latest&orientation=landscape
        order_by = 'order_by=latest'
        orientation = (f'&orientation={self.screen_orientation}'
                       if self.screen_orientation != 'any orientation' else '')
        keyword = determine_keyword()
        return (f'{UnsplashConfig.URL}/s/photos/'
                f'{keyword}?{order_by}{orientation}')

    def __get_html_of_image_grid(self):
        headers = {
            'User-Agent': UserAgent().chrome
        }
        response = requests.get(self.images_grid_url, headers=headers)
        return response.content

    def parse(self):
        html = self.__get_html_of_image_grid()
        soup = BeautifulSoup(html, features='lxml')
        # '//div[@data-test="search-photos-route"]//img'
        image_grid_soup = soup.find(
            'div', attrs={'data-test': 'search-photos-route'})
        images_tags = image_grid_soup.find_all('img')

        random_image_link = random.choice(images_tags)['src']

        image = requests.get(random_image_link, stream=True)
        print(dir(image))
        with open(os.path.join(self.path_for_image, 'pic1.jpg'), 'wb') as handler:
            handler.write(image.content)

    def download_random_image(self):
        self.parse()
