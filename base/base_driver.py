import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self, direction, pause_time=5, step_wait=3):
        if direction not in ["up", "down"]:
            raise ValueError("direction must be 'up' or 'down'")

        # wait a bit to let the page load initially
        time.sleep(pause_time)

        if direction == "down":
            last_height = -1
            while True:
                # scroll to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # wait for content to load
                time.sleep(step_wait)

                # get new scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight;")

                # if no new content, we've reached the bottom
                if new_height == last_height:
                    break
                last_height = new_height

        else:  # direction == "up"
            last_pos = -1
            while True:
                # scroll to top
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(step_wait)

                # check scroll position
                new_pos = self.driver.execute_script(
                    "return window.pageYOffset || document.documentElement.scrollTop;"
                )
                if new_pos == last_pos:
                    break
                last_pos = new_pos

        # small wait at the end to ensure page is fully stable
        time.sleep(3)

    def wait_for_invisible(self, locator_type, locator):
        wait= WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.invisibility_of_element_located((locator_type, locator)))
        return list_of_elements
    def wait_for_visible(self, locator_type, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        list_of_elements= wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return list_of_elements
    def wait_for_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return list_of_elements
    def wait_for_available_switch(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type, locator)))
        return list_of_elements