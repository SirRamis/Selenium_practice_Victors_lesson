import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from src.data import LOGIN, PASSWORD
from locators.locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.saucedemo.com/')
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    yield driver
    driver.quit()

