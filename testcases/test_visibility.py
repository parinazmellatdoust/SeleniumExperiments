import pytest
from pages.visibility_page import VisibilityPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestVisibility:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.visibility = VisibilityPage(self.driver)
        self.ut = Utils()

    def test_element_visibility_states(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/visibility")

        # 2. Action: Click the 'Hide' button
        self.visibility.click_hide_button()

        # 3. Verification: Determine if other buttons are visible or not

        # 'Removed' button: Detached -> Not Visible (False)
        self.ut.assert_true(not self.visibility.is_removed_button_visible(), "Removed button should not be visible")

        # 'Zero Width' button: Attached but 0 width -> Not Visible (False)
        self.ut.assert_true(not self.visibility.is_zero_width_button_visible(),
                            "Zero Width button should not be visible")

        # 'Overlapped' button: Visible but covered -> Visible (True)
        self.ut.assert_true(self.visibility.is_overlapped_button_visible(), "Overlapped button should be visible")

        # 'Invisible' button (visibility: hidden) -> Not Visible (False)
        self.ut.assert_true(not self.visibility.is_invisible_button_visible(), "Invisible button should not be visible")

        # 'Not Displayed' button (display: none) -> Not Visible (False)
        self.ut.assert_true(not self.visibility.is_not_displayed_button_visible(),
                            "Not Displayed button should not be visible")

        # 'Opacity 0' button: Opacity 0 -> Not Visible to Eye in Selenium (False)
        self.ut.assert_true(not self.visibility.is_opacity_zero_button_visible(),
                            "Opacity 0 button should not be visible")