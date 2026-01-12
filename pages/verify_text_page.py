from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class VerifyTextPage(BaseDriver):

    # --- Locators ---
    USERNAME_TEXT = "//div[@class='container']/div//span[text()='UserName']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_username_text(self):
        return self.wait_for_visible(By.XPATH, self.USERNAME_TEXT)

    # --- Action Methods ---

    def verify_username_exists(self):
        is_visible = self.get_username_text().is_displayed()
        self.log.debug(f"Verified 'UserName' text visibility: {is_visible}")
        return is_visible