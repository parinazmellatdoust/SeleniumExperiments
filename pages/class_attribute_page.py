from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ClassAttributePage(BaseDriver):

    # --- Locators ---
    # Use CSS Selector for better performance and reliability
    BLUE_BUTTON = ".btn-primary"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_blue_button(self):
        return self.wait_for_clickable(By.CSS_SELECTOR, self.BLUE_BUTTON)

    # --- Action Methods ---

    def click_blue_button(self):
        self.get_blue_button().click()
        self.log.debug("Clicked the blue button")