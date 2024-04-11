from selenium.webdriver.common.by import By

from practice.src import urls
from selenium.webdriver.support import expected_conditions as EC

ELEMENT_START_TEST = ("xpath", "//button[text()='Начать тестирование']")
HEADER_h1 = ("xpath", "/html/body/h1")

def test1_actual_text(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    actual_text = chrome.find_element(*HEADER_h1).text
    assert actual_text == 'Практика с ожиданиями в Selenium'

def test2_wait_elemet_start_test(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    visible_after_button = wait.until(EC.element_to_be_clickable((ELEMENT_START_TEST)))
    assert visible_after_button.text == 'Начать тестирование'

def test_registration(chrome):
    chrome.get(urls.Urls.reg_url)
    chrome.find_element(ELEMENT_START_TEST).click()

def test_checking_the_registration_functionality_on_the_site(chrome, wait):
    chrome.get(urls.Urls.reg_url)
    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Начать тестирование']")))
    assert visible_after_button.text == 'Начать тестирование'