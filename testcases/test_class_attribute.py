import pytest
from pages.class_attribute_page import ClassAttributePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestClassAttribute:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.class_attr = ClassAttributePage(self.driver)
        self.ut = Utils()

    def test_class_attribute_changes(self):
        # 1. Navigate
        self.driver.get("http://www.uitestingplayground.com/classattr")

        # 2. Action: Click the blue button
        self.class_attr.click_blue_button()