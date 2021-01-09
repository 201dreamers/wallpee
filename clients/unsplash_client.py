import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from misc import determine_keyword
from downloaders.ui.unsplash_page import UnsplashPage
from downloaders.parser.unsplash_parser import UnsplashParser


class UnsplashClient:

    __slots__ = ('path_for_image')

    def __init__(self, path_for_image) -> None:
        self.path_for_image = path_for_image

    def __create_driver(self) -> WebDriver:
        # Set options for automatic firefox downloading without any popups
        options = Options()
        options.set_preference(
            'browser.download.alwaysOpenInSystemViewerContextMenuItem', False)
        options.set_preference('browser.download.folderList', 2)
        options.set_preference(
            'browser.download.manager.showWhenStarting', False)
        options.set_preference('browser.download.dir', self.path_for_image)
        options.set_preference('browser.download.useDownloadDir', True)
        options.set_preference(
            'browser.helperApps.neverAsk.saveToDisk',
            ('image/gif,image/jpeg,image/pjpeg,image/png,'
             'image/svg+xml,image/tiff,image/webp')
        )

        # Create firefox driver instance with set of options
        driver = webdriver.Firefox(firefox_options=options)
        return driver

    def __download_random_image_with_ui(self) -> None:
        # Using driver, find and download image from unsplash.com to the
        #  'path_for_image' directory
        # Sleep in the end is needed if image is big and it requires
        # time for downloading
        # FIXME Replace sleep with something else
        with self.__create_driver() as driver:
            unsplash_page = UnsplashPage(driver)
            unsplash_page.open_page()
            unsplash_page.search(determine_keyword())
            unsplash_page.choose_orientation()
            unsplash_page.choose_sort_by_newest()
            unsplash_page.download_random_image()
            time.sleep(2)

        print(f'Image was saved to {self.path_for_image}')

    def __download_random_image_with_parser(self):
        unsplash_parser = UnsplashParser(self.path_for_image)
        unsplash_parser.download_random_image()

    def download_random_image(self, selenium: bool = False) -> None:
        if selenium:
            self.__download_random_image_with_ui()
        else:
            self.__download_random_image_with_parser()
