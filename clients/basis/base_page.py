from typing import List, Union

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementNotInteractableException

from clients.configs import DefaultConfig


class BasePage:
    """Base page for page object pattern realization.

    Has methods that wraps default methods from selenium"""

    __slots__ = ('driver')

    def __init__(self, driver):
        self.driver = driver

    def find_element(
        self, locator,
        timeout=DefaultConfig.TIMEOUT
    ) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(
        self, locator,
        timeout=DefaultConfig.TIMEOUT,
    ) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, web_element: WebElement, depth: int = 0) -> bool:
        if depth > 4:
            return False
        try:
            web_element.click()
            return True
        except ElementNotInteractableException:
            page = self.driver.find_element_by_tag_name('html')
            page.send_keys(Keys.PAGE_DOWN)
            return self.click(web_element, depth=depth + 1)
