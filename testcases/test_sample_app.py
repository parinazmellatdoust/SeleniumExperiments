import pytest
from pages.sample_app_page import SampleAppPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSampleApp:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sample_app = SampleAppPage(self.driver)
        self.ut = Utils()

    # --- Positive Test Case ---
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "test_case",
        Utils.load_json("sample_app_positive.json"),
        ids=lambda x: x["description"]
    )
    def test_successful_login(self, test_case):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/sampleapp")

        # 2. Extract data
        username = test_case["username"]
        password = test_case["password"]

        # 3. Perform Login
        self.sample_app.perform_login(username, password)

        # 4. Verification
        logout_btn = self.sample_app.get_logout_button()
        self.ut.assert_true(logout_btn.is_displayed(), "Logout button not found.")

        status_msg = self.sample_app.get_status_message()
        status_text = status_msg.text
        self.ut.assert_text_equals(status_text, f"Welcome, {username}!", "Welcome message missing.")

    # --- Negative Test Case ---
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "test_case",
        Utils.load_json("sample_app_negative.json"),
        ids=lambda x: x["description"]
    )
    def test_failed_login(self, test_case):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/sampleapp")

        # 2. Extract data
        username = test_case["username"]
        password = test_case["password"]

        # 3. Perform Login
        self.sample_app.perform_login(username, password)

        # 4. Verification
        status_element = self.sample_app.get_status_message()
        error_message = status_element.text

        # Verify exact error message
        self.ut.assert_text_equals(error_message, "Invalid username/password", "Error message mismatch")