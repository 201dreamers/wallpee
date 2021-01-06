from typing import List, Optional

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementNotInteractableException

from clients.configs import DefaultConfig


class BasePage:

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
        depth=0
    ) -> Optional[List[WebElement]]:
        try:
            elems = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except ElementNotInteractableException:
            if depth >= 4:
                return []
            html = self.driver.find_element_by_tag_name('html')
            html.send_keys(Keys.PAGE_DOWN)
            elems = self.find_elements(locator, depth=depth + 1)
        return elems
