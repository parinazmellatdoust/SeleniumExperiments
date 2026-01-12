from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class OverlappedPage(BaseDriver):
    # --- Locators ---
    # Corrected: Use just the ID string 'name', not '#name'
    NAME_INPUT = "name"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_name_input(self):
        # Use find_element directly, no wait needed as we scroll immediately
        return self.driver.find_element(By.ID, self.NAME_INPUT)

    # --- Action Methods ---

    def enter_name(self, name):
        # Find the element
        element = self.get_name_input()

        # Scroll to element before typing
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # Clear and type
        element.clear()
        element.send_keys(name)
        self.log.debug(f"Entered name: {name}")

    def get_input_value(self):
        return self.get_name_input().get_attribute("value")