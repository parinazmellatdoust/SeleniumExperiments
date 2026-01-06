from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SampleAppPage(BaseDriver):
    # --- Locators ---
    USERNAME_INPUT = "//input[@name='UserName']"
    PASSWORD_INPUT = "//input[@name='Password']"

    # The Login Button ID remains 'login' even after logging in
    LOGIN_BUTTON = "//button[@id='login']"

    # We must use XPath to find the button with the specific text 'Log Out'.
    LOGOUT_BUTTON = "//button[@id='login' and text()='Log Out']"

    STATUS_MESSAGE = "//label[@id='loginstatus']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Get Methods ---

    def get_username_input(self):
        return self.wait_for_visible(By.XPATH, self.USERNAME_INPUT)

    def get_password_input(self):
        return self.wait_for_visible(By.XPATH, self.PASSWORD_INPUT)

    def get_login_button(self):
        return self.wait_for_clickable(By.XPATH, self.LOGIN_BUTTON)

    def get_logout_button(self):
        return self.driver.find_element(By.XPATH, self.LOGOUT_BUTTON)

    def get_status_message(self):
        return self.wait_for_visible(By.XPATH, self.STATUS_MESSAGE)

    # --- Action Methods ---
    def enter_username(self, username):
        self.get_username_input().clear()
        self.get_username_input().send_keys(username)
        self.log.debug(f"Entered username: {username}")

    def enter_password(self, password):
        self.get_password_input().clear()
        self.get_password_input().send_keys(password)
        self.log.debug(f"Entered password: {password}")

    def click_login(self):
        self.get_login_button().click()
        self.log.debug("Clicked Login button")

    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()