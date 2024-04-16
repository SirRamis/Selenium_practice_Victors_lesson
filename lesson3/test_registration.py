import time
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from practice.src import urls
from selenium.webdriver.support import expected_conditions as EC

START_TEST_BUTTON = ("xpath", "//button[text()='Начать тестирование']")
HEADER_h1 = ("xpath", "/html/body/h1")
REG_FORM = ("xpath", '//*[@id="registrationForm"]/label[1]')
USERNAME_FIELD = ('xpath', '//*[@id="login"]')
PASSWORD_FIELD = ('xpath', '//*[@id="password"]')
AGREE = ('xpath', '//*[@id="agree"]')
REG_BUTTON = ("xpath", '//*[@id="register"]')
MESSAGE = ('xpath', '//*[@id="successMessage"]')

@allure.title('test text')
@allure.description('проверяет текст')
@allure.severity(allure.severity_level.BLOCKER)
def test1_actual_text(chrome, wait):
    """
    Это через дроп стрингу
    :param chrome:
    :param wait:
    :return:
    """
    chrome.get(urls.Urls.reg_url)
    actual_text = chrome.find_element(*HEADER_h1).text
    assert actual_text == 'Практика с ожиданиями в Selenium'
@allure.title('test2 text')
@allure.description('проверяет текст2')
@allure.severity(allure.severity_level.BLOCKER)
def test2_wait_elemet_start_test(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    visible_after_button = wait.until(EC.element_to_be_clickable((START_TEST_BUTTON)))
    assert visible_after_button.text == 'Начать тестирование'

def test3_registration(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    wait.until(EC.element_to_be_clickable((START_TEST_BUTTON)))
    chrome.find_element(*START_TEST_BUTTON).click()
    time.sleep(3)
    visible_after_button = chrome.find_element(*REG_FORM).text
    assert visible_after_button == 'Логин:'

def test4_registration(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    wait.until(EC.element_to_be_clickable((START_TEST_BUTTON)))
    chrome.find_element(*START_TEST_BUTTON).click()
    time.sleep(3)
    chrome.find_element(*USERNAME_FIELD).send_keys("login")
    chrome.find_element(*PASSWORD_FIELD).send_keys("password")
    chrome.find_element(*AGREE).click()
    chrome.find_element(*REG_BUTTON).click()
    time.sleep(4)
    expected_text = chrome.find_element(*MESSAGE).text
    actual_text = 'Вы успешно зарегистрированы!'
    assert expected_text == actual_text

def test1_add(chrome):
    chrome.get('https://the-internet.herokuapp.com/add_remove_elements/')
    chrome.find_element('xpath','//*[@id="content"]/div/button').click()
    a = chrome.find_element('xpath','//*[@id="elements"]/button')
    assert a.is_displayed()

def test1_add_delete(chrome):
    chrome.get('https://the-internet.herokuapp.com/add_remove_elements/')
    time.sleep(3)
    chrome.find_element('xpath','//*[@id="content"]/div/button').click()
    chrome.find_element('xpath','//*[@id="elements"]/button').click()
    time.sleep(3)
    assert not chrome.find_elements('xpath', '//*[@id="elements"]/button'), 'В корзине есть товары'


def test2_auth(chrome):
    username = "admin"
    password = "admin"
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    chrome.get(url)
    time.sleep(3)
    expected_text = chrome.find_element('xpath','//*[@id="content"]/div/p').text
    assert expected_text == 'Congratulations! You must have the proper credentials.', "Registration was not successful"

    # # Ждем появления элемента на странице с помощью WebDriverWait
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, "h3"))  # Пример: ждем появления элемента <h3>
    #     )
    #     print("Элемент появился на странице:", element.text)
    # except:
    #     print("Элемент не появился на странице")
    # finally:
    #     driver.quit()

from PIL import Image

image_path = "https://the-internet.herokuapp.com/broken_images" # Укажите путь к вашему изображению
def test_check_image_integrity(chrome):
    chrome.get('https://the-internet.herokuapp.com/broken_images')
    time.sleep(3)
    try:
        with Image.open('https://the-internet.herokuapp.com/img/avatar-blank.jpg') as img:
            width, height = img.size
            if width > 0 and height > 0:
                print("Изображение целостное.")
            else:
                print("Изображение повреждено или не может быть загружено.")
    except Exception as e:
        print("Ошибка при загрузке изображения:", e)

        images = chrome.execute_script("return document.getElementsByTagName('img');")
        for image in images:
            src = image.get_attribute("src")
            width = chrome.execute_script("return arguments[0].naturalWidth;", image)
            if width == 0:
                print(f"Broken image found: {src}")


def test_color(chrome):
    chrome.get("https://www.selenium.dev/selenium/web/colorPage.html")
    cssValue = chrome.find_element(By.ID, "namedColor").value_of_css_property('background-color')
    assert cssValue == 'rgba(0, 128, 0, 1)'