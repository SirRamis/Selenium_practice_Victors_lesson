import time

from selenium.webdriver.common.by import By
#from conftest import *

from practice.locators.locators import ADDITEM_BUTTON, ITEMINCART_FIELD


from pages.login_page import LoginPage
from src.urls import Urls


class TestLogin:
    url = Urls()

    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        time.sleep(4)
        actual_text = driver.find_element(*TITLE).text
        expected_text = "Products"
        assert actual_text == expected_text
        time.sleep(4)


    def test_login1(driver):
        cards = driver.find_elements(*CARDS)
        assert len(cards) == 6
        time.sleep(4)
# def test_registration(driver1):
#     driver1.get(url=urls.reg_url)

def test_add_item(chrome, login1):
    chrome.find_element(*ADDITEM_BUTTON).click()
    actual_text = chrome.find_element(*ITEMINCART_FIELD).text
    assert actual_text

# def test_add_item(chrome):
#     login(chrome, "Artem", PASSWORD)
#     chrome.find_element(*ADDITEM_BUTTON).click()
#     actual_text = chrome.find_element(*ITEMINCART_FIELD).text
#     assert actual_text

def test4_deleit_item(driver):
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()  # Удаляет с корзины
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'


def test5_added_item_in_cart(driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Добавляет в карзину из карточки
    time.sleep(2)
    assert driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине нет товаров'


def test6_deleit_item_in_cart(driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Добавляет в карзину из карточки
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Удаляет с корзины через карточку товара
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'
    time.sleep(4)


def test7_go_to_card(driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку через картинку
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', "Элемент не выбран"
    # select_element = browser.find_element('//*[@id="item_4_img_link"]')
    # Проверим, был ли элемент выбран
    # if select_element.is_selected():
    #     print("Элемент выбран")
    # else:
    #     print("Элемент не выбран")


def test8_go_to_card2(driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]').click()  # переход к карточке товара после клика по названию товара
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', "Элемент не выбран"
