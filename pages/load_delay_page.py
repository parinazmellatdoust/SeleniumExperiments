from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class LoadDelayPage(BaseDriver):

    # --- Locators ---
    BUTTON = "//button[contains(text(), 'Button Appearing After Delay')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_button(self):
        return self.wait_for_clickable(By.XPATH, self.BUTTON)

    # --- Action Methods ---

    def click_button(self):
        self.get_button().click()
        self.log.debug("Clicked button appearing after delay")