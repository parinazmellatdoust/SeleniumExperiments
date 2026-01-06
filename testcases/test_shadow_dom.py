import pytest
import time
from pages.shadow_dom_page import ShadowDomPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestShadowDom:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.shadow_dom = ShadowDomPage(self.driver)
        self.ut = Utils()

    def test_shadow_dom_interaction(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/shadowdom")

        # 2. Action: Click the button using JavaScript
        self.shadow_dom.click_guid_button()

        # 3. Wait for generation
        time.sleep(1)

        # 4. Verification
        actual_text = self.shadow_dom.get_generated_guid_label()

        # Assert that text is not empty (meaning generation happened)
        self.ut.assert_true(len(actual_text) > 0, f"GUID generation failed. Text was empty.")