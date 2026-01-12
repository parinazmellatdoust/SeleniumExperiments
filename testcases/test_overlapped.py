import pytest
from pages.overlapped_page import OverlappedPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestOverlapped:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.overlapped = OverlappedPage(self.driver)
        self.ut = Utils()

    def test_overlapped_element_type_text(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/overlapped")

        # 2. Action: Scroll and enter text into the Name field
        test_name = "Selenium"
        self.overlapped.enter_name(test_name)

        # 3. Verification: Ensure the text was entered correctly
        actual_value = self.overlapped.get_input_value()
        self.ut.assert_text_equals(actual_value, test_name, "Input value did not match.")