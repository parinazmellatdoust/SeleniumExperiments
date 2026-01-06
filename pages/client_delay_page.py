from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class ClientDelayPage(BaseDriver):

    # --- Locators ---
    BUTTON_TRIGGER = "//button[text()='Button Triggering Client Side Logic']"
    AJAX_DATA_LABEL = "//p[contains(text(), 'Data calculated')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_trigger_button(self):
        return self.wait_for_clickable(By.XPATH, self.BUTTON_TRIGGER)

    def get_ajax_data_label(self):
        # Pass 20 seconds specifically for this slow element
        return self.wait_for_visible(By.XPATH, self.AJAX_DATA_LABEL, time=20)

    # --- Action Methods ---

    def click_trigger_button(self):
        self.get_trigger_button().click()
        self.log.debug("Clicked Trigger button. Waiting for AJAX response...")