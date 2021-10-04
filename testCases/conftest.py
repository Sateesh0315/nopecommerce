import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver
