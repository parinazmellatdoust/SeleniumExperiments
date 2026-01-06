import pytest
from pages.hidden_layers_page import HiddenLayersPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestHiddenLayers:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hidden_layers = HiddenLayersPage(self.driver)
        self.ut = Utils()

    def test_hidden_layers_flow(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/hiddenlayers")

        # 2. Click the Green Button (Visible top layer)
        self.hidden_layers.click_green_button()

        # 3. Wait for Blue Button to be accessible (Implicitly confirms Green is gone)
        self.hidden_layers.wait_until_blue_is_clickable()

        # 4. Action: Click the Blue Button (Now revealed)
        self.hidden_layers.click_blue_button()

        # 5. Verification: Ensure the Blue button is still displayed/interactable
        blue_btn = self.hidden_layers.get_blue_button()
        self.ut.assert_true(blue_btn.is_displayed(), "Blue button should be displayed")