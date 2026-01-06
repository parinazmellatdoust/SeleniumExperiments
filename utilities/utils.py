import inspect
import logging
import os
import json


class Utils:

    # --- Standard Assertions (Pytest Compatible) ---

    def assert_text_equals(self, actual_text, expected_text, log_msg=""):
        assert actual_text == expected_text, f"{log_msg} | Expected '{expected_text}' but got '{actual_text}'"

    def assert_true(self, condition, log_msg=""):
        assert condition, log_msg

    # --- Logger ---
    @staticmethod
    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Check if handlers already exist to prevent duplicate logs
        if not logger.handlers:
            fh = logging.FileHandler('test.log', mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger

    # --- JSON Loader ---
    @staticmethod
    def load_json(file_name):
        base_path = os.path.dirname(os.path.dirname(__file__))
        json_path = os.path.join(base_path, "testdata", file_name)

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data