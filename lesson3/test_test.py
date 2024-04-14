import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driv(chrome_options):
    driv = webdriver.Chrome(options=chrome_options)
    return driv

@pytest.fixture
def wait(driv):
    wait = WebDriverWait(driv, timeout=10)
    return wait

def test_visible_after_with_explicit_waits(driv, wait):
    driv.get('https://demoqa.com/dynamic-properties')
    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Visible After 5 Seconds']")))
    assert visible_after_button.text == 'Visible After 5 Seconds'



# Инициализация драйвера браузера
def test_qw():
    driver = webdriver.Chrome()
    driver.get("https://<username>:<password>@the-internet.herokuapp.com/basic_authl")
    #driver.get("https://the-internet.herokuapp.com/basic_authl")


def test_qwt():
    username = "your_username"
    password = "your_password"

    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()
    # Формируем URL для авторизации HTTP Basic
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    time.sleep(3)
    # Переходим по URL
    driver.get(url)

