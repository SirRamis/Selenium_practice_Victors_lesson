import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from practice.src import urls
from practice.src.data import LOGIN, PASSWORD
from practice.locators.locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(urls.Urls.main_url)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    yield driver
    driver.quit()
@pytest.fixture
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service)
    yield chrome
    chrome.quit()

@pytest.fixture
def wait(chrome):
    wait = WebDriverWait(chrome, timeout=10)
    return wait
@pytest.fixture
def login1(chrome):
    chrome.get(urls.Urls.main_url)
    chrome.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    chrome.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    chrome.find_element(*LOGIN_BUTTON).click()
def login(chr: webdriver.Chrome, username, password):
    chr.get(urls.Urls.main_url)
    chr.find_element(*USERNAME_FIELD).send_keys(username)
    chr.find_element(*PASSWORD_FIELD).send_keys(password)
    chr.find_element(*LOGIN_BUTTON).click()

