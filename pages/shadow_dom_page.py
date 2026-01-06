from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ShadowDomPage(BaseDriver):
    # --- Locators ---
    SHADOW_HOST = "button-text"
    EDIT_FIELD_INPUT = "editField"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = Utils.custom_logger()

    # --- Action Methods ---

    def click_guid_button(self):
        self.log.debug("Executing JS to Force Click button inside Shadow DOM")

        # Script:
        # 1. Scans ALL elements on the page for a Shadow Root.
        # 2. Checks if that root contains our button.
        # 3. Dispatches a MouseEvent (Real Click) to it.
        script = """
            var allElements = document.querySelectorAll('*');
            var found = false;

            for (var i = 0; i < allElements.length; i++) {
                if (allElements[i].shadowRoot) {
                    var root = allElements[i].shadowRoot;
                    var button = root.querySelector('#buttonGenerate');

                    if (button) {
                        // Instead of simple button.click(), we dispatch a MouseEvent.
                        // This ensures the browser recognizes it as a user interaction.
                        var event = new MouseEvent('click', {
                            bubbles: true,
                            cancelable: true,
                            view: window
                        });
                        button.dispatchEvent(event);
                        found = true;
                        break;
                    }
                }
            }
            return found;
        """

        # Check if the script actually found and clicked the button
        clicked = self.driver.execute_script(script)
        if not clicked:
            self.log.error("Button not found in any Shadow Root!")
        else:
            self.log.debug("Shadow button clicked via MouseEvent")

    # --- Get Methods ---

    def get_generated_guid_label(self):
        self.log.debug("Executing JS to read value from Input inside Shadow DOM")

        # Use the same robust loop to find the input
        script = """
            var allElements = document.querySelectorAll('*');
            var value = "";

            for (var i = 0; i < allElements.length; i++) {
                if (allElements[i].shadowRoot) {
                    var root = allElements[i].shadowRoot;
                    var input = root.querySelector('#editField');
                    if (input) {
                        value = input.value;
                        break;
                    }
                }
            }
            return value;
        """

        return self.driver.execute_script(script)