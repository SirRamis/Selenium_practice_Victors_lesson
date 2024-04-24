import time
from pprint import pprint

from selenium.webdriver.common.by import By
from selenium import webdriver



def met_5_6_1():
    url = 'https://parsinger.ru/methods/1/index.html'
    driver = webdriver.Chrome()

    try:
        for i in range(100):
            driver.get(url)
            driver.refresh()
            result_element = driver.find_element(By.ID, 'result')
            result_text = result_element.text
            if result_text != 'refresh page':
                result_element = driver.find_element(By.ID, 'result')
                result_text = result_element.text
                print(result_text)
                break
    finally:
        driver.quit()
#met_5_6_1()
def met_5_6_2():
    driver = webdriver.Chrome()
    url = 'https://parsinger.ru/selenium/5.5/1/1.html'
    driver.get(url)
    el_numbers = driver.find_elements(By.XPATH, '//*[@id="textfields-container"]/input')
    for i in el_numbers:
        i.get_attribute('value')
        i.clear()
    driver.find_element(By.XPATH, '//*[@id="checkButton"]').click()
    # Переключаемся на алерт
    alert = driver.switch_to.alert
    # Получаем текст с алерта
    alert_text = alert.text
    print(alert_text)
    driver.quit()
#met_5_6_2()
def met_5_6_3():
    url = 'https://parsinger.ru/methods/3/index.html'
    driver = webdriver.Chrome()
    driver.get(url)
    cookies = driver.get_cookies()
    #pprint(cookies)
    q = []
    for cookie in cookies:
        name = cookie['name']
        value = cookie['value']
        b = name.split('_')
        c = int(b[2])
        if c % 2 == 0:
            q.append(int(cookie['value']))
    print(sum(q))
#met_5_6_3()
def met_5_6_4():
    url = 'https://parsinger.ru/selenium/5.5/2/1.html'
    driver = webdriver.Chrome()
    driver.get(url)
    el_numbers = driver.find_elements(By.XPATH, '//*[@id="textfields-container"]/input')
    for i in el_numbers:
        a = i.get_attribute('disabled')
        if a != 'true':
            i.clear()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkButton"]').click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()
    time.sleep(3)
    driver.quit()
met_5_6_4()
