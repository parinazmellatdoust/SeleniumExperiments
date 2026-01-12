from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class MouseOverPage(BaseDriver):

    # --- Locators ---
    CLICK_COUNT = "clickCount"
    CLICK_ME_LINK = "//a[contains(text(), 'Click me')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_click_count(self):
        return self.wait_for_visible(By.ID, self.CLICK_COUNT)

    def get_click_me_link(self):
        return self.wait_for_clickable(By.XPATH, self.CLICK_ME_LINK)

    # --- Action Methods ---

    def click_click_me_link(self):
        self.get_click_me_link().click()
        self.log.debug("Clicked 'Click me' link")