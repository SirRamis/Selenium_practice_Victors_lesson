import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def one():
    url = 'https://parsinger.ru/selenium/3/3.html'
    driver = webdriver.Chrome()
    driver.get(url)
    p_elements = (By.XPATH, '//div[@class="text"]')
    numbers = 0
    for p_element in p_elements:
        text = p_element.text
        for num in text.split():
            numbers += numbers
    print(numbers)
    time.sleep(3)
one()uytyutyt