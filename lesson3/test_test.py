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
    driver.get("https://the-internet.herokuapp.com/basic_authl")


def test_qwt():
    username = "your_username"
    password = "your_password"

    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()
    time.sleep(3)
    # Формируем URL для авторизации HTTP Basic
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    time.sleep(3)
    # Переходим по URL
    driver.get(url)

    # Продолжайте ваш тест здесь...

# Загрузка страницы
#driver.get("https://the-internet.herokuapp.com/basic_authl")

# Ожидание появления всплывающего окна
# popup_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "your_popup_xpath"))
# )
#
# # Находим поля ввода для имени пользователя и пароля
# username_field = popup_element.find_element(By.XPATH, "your_username_input_xpath")
# password_field = popup_element.find_element(By.XPATH, "your_password_input_xpath")
#
# # Вводим логин и пароль
# username_field.send_keys("your_username")
# password_field.send_keys("your_password")
#
# # Находим кнопку входа и кликаем на нее
# login_button = popup_element.find_element(By.XPATH, "your_login_button_xpath")
# login_button.click()


