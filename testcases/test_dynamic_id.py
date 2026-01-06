import pytest
from pages.dynamic_id_page import DynamicIDPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestDynamicID:

    # --- Class Setup ---
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.dynamic_id_page = DynamicIDPage(self.driver)
        self.ut = Utils()

    def test_click_dynamic_button(self):
        # 1. Navigate to the URL
        self.driver.get("http://www.uitestingplayground.com/dynamicid")

        # 2. Call the action method from the Page Object
        self.dynamic_id_page.click_button_with_dynamic_id()