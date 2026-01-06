import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request, browser, url):
    # 1. Initialize Driver with automatic management
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        # Raise an error if an unsupported browser is passed
        raise pytest.UsageError(f"Browser '{browser}' is not supported. Use 'chrome' or 'edge'.")

    # 2. Navigate and maximize
    driver.get(url)
    driver.maximize_window()

    # 3. Assign driver to the test class (Standard POM practice)
    request.cls.driver = driver

    # 4. Yield control back to the test, then cleanup
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", default="http://www.uitestingplayground.com/")


# Fixtures to capture the command line arguments
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")