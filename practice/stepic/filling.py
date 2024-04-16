import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = (By.XPATH, '/html/body/div[1]/div/div[3]/input')
lname = (By.XPATH, '/html/body/div[1]/div/div[4]/input')
fname = (By.XPATH, '/html/body/div[1]/div/div[5]/input')
old = (By.XPATH, '/html/body/div[1]/div/div[6]/input')
sity = (By.XPATH, '/html/body/div[1]/div/div[7]/input')
email = (By.XPATH, '/html/body/div[1]/div/div[8]/input')
button = (By.XPATH, '//*[@id="btn"]')
url = 'https://parsinger.ru/selenium/1/1.html'
url1 = 'https://parsinger.ru/selenium/2/2.html'


def fill():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(*name).send_keys('a')
    driver.find_element(*lname).send_keys('b')
    driver.find_element(*fname).send_keys('c')
    driver.find_element(*old).send_keys(23)
    driver.find_element(*sity).send_keys('Abc')
    driver.find_element(*email).send_keys('abc@abc.com')
    driver.find_element(*button).click()
    print(driver.find_element(By.ID, 'result').text)
    #input()
    time.sleep(5)

fill()

def num_element():
    driver = webdriver.Chrome()
    driver.get(url1)
    for i in driver.find_element(By.ID, 'href')
