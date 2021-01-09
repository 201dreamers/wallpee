from random import choice
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from downloaders.ui.base_page import BasePage
from config import UnsplashConfig
from misc import determine_screen_orientation


class UnsplashPage(BasePage):
    """Represents page from https://unsplash.com with methods that is needed
    for downloading image"""

    __slots__ = ('driver', 'orientation')

    SEARCH_FIELD: tuple = (By.NAME, 'searchKeyword')
    ORIENTATION_DROPDOWN: tuple = (
        By.CSS_SELECTOR,
        '#popover-search-orientation-filter > button:nth-child(1)',
    )
    ORIENTATION_LIST_ITEMS: tuple = (
        By.XPATH,
        '//div[@class="_2HZSj _2b4s_ _1mPfo _16e5w _2YS8p"]/ul/li',
    )
    SORTBY_DROPDOWN: tuple = (
        By.XPATH,
        '//div[@id="popover-search-order-filter"]/button',
    )
    SORTBY_LIST_ITEMS: tuple = (
        By.XPATH,
        '//div[@class="_2HZSj _2b4s_ _1mPfo _16e5w _2YS8p"]//li',
    )
    IMAGES_GRID: tuple = (
        By.XPATH,
        '//div[@data-test="search-photos-route"]//img'
    )
    IMAGE_SIZES_DROPDOWN: tuple = (
        By.XPATH,
        '//div[@id="popover-download-button"]//button'
    )
    IMAGE_SIZES: tuple = (
        By.XPATH,
        '//div[@class="_2HZSj _2_izy _16e5w _12nqk _2YS8p"]//li'
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.orientation: str = determine_screen_orientation().capitalize()

    def open_page(self) -> None:
        """Open main page of site unsplash.com"""
        self.driver.get(UnsplashConfig.URL)

    def search(self, keyword: str) -> None:
        """Input some data into search field and press ENTER"""
        search_field = self.find_element(self.SEARCH_FIELD)
        search_field.send_keys(keyword, Keys.RETURN)

    def choose_orientation(self) -> None:
        """Choose orientation from dropdown unordered list on page"""
        # Open orientation chooser
        self.click(self.find_element(self.ORIENTATION_DROPDOWN))

        # Find needed orientation from list and click it
        orientation_list_items = self.find_elements(
            self.ORIENTATION_LIST_ITEMS)
        for elem in orientation_list_items:
            if elem.text == self.orientation:
                self.click(elem)
                break

    def choose_sort_by_newest(self):
        """Choose sorting order from dropdown unordered list on page"""
        # Open 'sort by' chooser
        self.click(self.find_element(self.SORTBY_DROPDOWN))

        # Select 'Newest' from list
        sortby_list_items = self.find_elements(self.SORTBY_LIST_ITEMS)
        for elem in sortby_list_items:
            if elem.text == 'Newest':
                self.click(elem)
                break

    def get_list_of_images(self) -> List[WebElement]:
        """Find images grid and return list of img elements"""
        images_grid = self.find_elements(self.IMAGES_GRID)
        return images_grid

    def download_random_image(self) -> None:
        """Downloads image from unsplash that is closest to the
        monitor size"""
        # Choose image from list of images and click on it
        random_image = choice(self.get_list_of_images())
        ok = self.click(random_image)
        # If can't click on image choose another and try to click
        if not ok:
            random_image = choice(self.get_list_of_images())
            self.click(random_image)

        # Click on the dropdown button and select the closest value
        self.click(self.find_element(self.IMAGE_SIZES_DROPDOWN))
        image_sizes = self.find_elements(self.IMAGE_SIZES)

        def get_sizes_difference(size_web_element):
            size = tuple(size_web_element.text.split(' ')[-1]
                         .removeprefix('(').removesuffix(')').split('x'))
            return abs(
                abs(int(size[0]) - self.monitor.width)
                - abs(int(size[1]) - self.monitor.height)
            )

        # Get closest value from list to screen size
        closest_value = min(image_sizes, key=get_sizes_difference)
        self.click(closest_value)
