from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class HiddenLayersPage(BaseDriver):

    # --- Locators ---
    GREEN_BUTTON = "greenButton"
    BLUE_BUTTON = "blueButton"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_green_button(self):
        return self.wait_for_clickable(By.ID, self.GREEN_BUTTON)

    def get_blue_button(self):
        return self.wait_for_clickable(By.ID, self.BLUE_BUTTON)

    # --- Action Methods ---

    def click_green_button(self):
        self.get_green_button().click()
        self.log.debug("Clicked Green button")

    def wait_until_blue_is_clickable(self):
        # we wait for Blue to become clickable. This proves Green is gone.
        self.wait_for_clickable(By.ID, self.BLUE_BUTTON)
        self.log.debug("Blue button is now ready to be clicked")

    def click_blue_button(self):
        # but let's call the getter to be safe and clean
        self.get_blue_button().click()
        self.log.debug("Clicked Blue button")