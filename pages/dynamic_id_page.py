from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class DynamicIDPage(BaseDriver):
    # --- Locators ---
    # Defined as class constants (Strings) to match your LaunchPage style
    BUTTON_WITH_DYNAMIC_ID = "//button[text()='Button with Dynamic ID']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Actions ---

    # 1. The 'Get' method: Finds the element using your BaseDriver wait
    def get_button_with_dynamic_id(self):
        return self.wait_for_clickable(By.XPATH, self.BUTTON_WITH_DYNAMIC_ID)

    # 2. The 'Action' method: Calls the get method and interacts
    def click_button_with_dynamic_id(self):
        self.get_button_with_dynamic_id().click()
        self.log.debug("Clicked button with dynamic ID")