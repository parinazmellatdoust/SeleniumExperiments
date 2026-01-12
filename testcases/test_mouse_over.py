import pytest
from pages.mouse_over_page import MouseOverPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestMouseOver:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.mouse_over = MouseOverPage(self.driver)
        self.ut = Utils()

    def test_consecutive_clicks(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/mouseover")

        # 2. Action: Click the link twice consecutively
        self.mouse_over.click_click_me_link()
        self.mouse_over.click_click_me_link()

        # 3. Verification: Check if click count is correct (2 clicks)
        count_text = self.mouse_over.get_click_count().text
        self.ut.assert_text_equals(count_text, "2", "Click count mismatch")