import pytest
from pages.client_delay_page import ClientDelayPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestClientDelay:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.client_delay = ClientDelayPage(self.driver)
        self.ut = Utils()

    def test_ajax_data_appears(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/clientdelay")

        # 2. Click Trigger
        self.client_delay.click_trigger_button()

        # 3. Wait for and Verify the data
        # The get_ajax_data_label method contains the explicit wait logic
        data_label = self.client_delay.get_ajax_data_label()
        actual_text = data_label.text

        # Verify the data is correct
        expected_text = "Data calculated on the client side."
        self.ut.assert_text_equals(actual_text, expected_text, "AJAX data text mismatch")