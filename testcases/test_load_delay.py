import pytest
from pages.load_delay_page import LoadDelayPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestLoadDelay:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.load_delay = LoadDelayPage(self.driver)
        self.ut = Utils()

    def test_load_delay_button_click(self):
        # 1. Navigate to the URL
        self.driver.get("http://www.uitestingplayground.com/loaddelay")

        # 2. Action: Click the button
        self.load_delay.click_button()