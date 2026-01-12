import pytest
from pages.nonbreaking_space_page import NonBreakingSpacePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestNonBreakingSpace:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.nbs = NonBreakingSpacePage(self.driver)
        self.ut = Utils()

    def test_nonbreaking_space_button_click(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/nbsp")

        # 2. Action: Click the button
        self.nbs.click_button()