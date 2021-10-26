import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    driver.get("https://www.sans.org/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


