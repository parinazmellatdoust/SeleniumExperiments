import pytest
from pages.verify_text_page import VerifyTextPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestVerifyText:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.verify_text = VerifyTextPage(self.driver)
        self.ut = Utils()

    def test_verify_text_uses_bold_style(self):
        # 1. Navigate to the URL
        self.driver.get("http://www.uitestingplayground.com/verifytext")

        # 2. Verification: Verify the specific text "UserName" is present
        is_present = self.verify_text.verify_username_exists()

        # Assert that the text is visible
        self.ut.assert_true(is_present, "The 'UserName' text was not found on the page.")