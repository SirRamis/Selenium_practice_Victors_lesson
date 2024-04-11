import time

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


def test1_actual_text(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    actual_text = chrome.find_element(*HEADER_h1).text
    assert actual_text == 'Практика с ожиданиями в Selenium'

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
