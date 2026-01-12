from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class VisibilityPage(BaseDriver):

    # --- Locators ---
    # Corrected: Removed '#' from ID strings to work with By.ID
    HIDE_BUTTON = "hideButton"
    REMOVED_BUTTON = "removedButton"
    ZERO_WIDTH_BUTTON = "zeroWidthButton"
    OVERLAPPED_BUTTON = "overlappedButton"
    INVISIBLE_BUTTON = "invisibleButton"
    NOT_DISPLAYED_BUTTON = "notdisplayedButton"
    OPACITY_ZERO_BUTTON = "transparentButton"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_hide_button(self):
        return self.wait_for_clickable(By.ID, self.HIDE_BUTTON)

    def get_removed_button(self):
        return self.wait_for_present(By.ID, self.REMOVED_BUTTON)

    def get_zero_width_button(self):
        return self.wait_for_present(By.ID, self.ZERO_WIDTH_BUTTON)

    def get_overlapped_button(self):
        return self.wait_for_present(By.ID, self.OVERLAPPED_BUTTON)

    def get_invisible_button(self):
        return self.wait_for_present(By.ID, self.INVISIBLE_BUTTON)

    def get_not_displayed_button(self):
        return self.wait_for_present(By.ID, self.NOT_DISPLAYED_BUTTON)

    def get_opacity_zero_button(self):
        return self.wait_for_present(By.ID, self.OPACITY_ZERO_BUTTON)

    # --- Helper for present ---
    def wait_for_present(self, locator_type, locator):
        # Standard presence check
        return self.driver.find_element(locator_type, locator)

    # --- Action Methods ---

    def click_hide_button(self):
        self.get_hide_button().click()
        self.log.debug("Clicked Hide button")

    def is_removed_button_visible(self):
        try:
            return self.get_removed_button().is_displayed()
        except:
            return False

    def is_zero_width_button_visible(self):
        return self.get_zero_width_button().is_displayed()

    def is_overlapped_button_visible(self):
        return self.get_overlapped_button().is_displayed()

    def is_invisible_button_visible(self):
        return self.get_invisible_button().is_displayed()

    def is_not_displayed_button_visible(self):
        return self.get_not_displayed_button().is_displayed()

    def is_opacity_zero_button_visible(self):
        return self.get_opacity_zero_button().is_displayed()