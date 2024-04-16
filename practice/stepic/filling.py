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
    time.sleep(5)

#fill()

def num_element():
    driver = webdriver.Chrome()
    driver.get(url1)

    driver.find_element(By.LINK_TEXT, '16243162441624').click()
    print(driver.find_element(By.ID, 'result').text)
    time.sleep(3)

#num_element()


# driver = webdriver.Chrome()
# driver.get('https://parsinger.ru/selenium/3/3.html')
#
# # Найдем все элементы с классом 'text'
# elements = driver.find_elements(By.CLASS_NAME, 'text')
# print(*elements)
# # Пройдемся по всем найденным элементам и выведем их содержимое
# for element in elements:
#     # Получаем текст элемента
#     text = element.text
#     # Разделяем текст на отдельные числа и преобразуем их в целые числа
#     numbers = [int(num) for num in text.split()]
#     # Выводим сумму чисел
#     print(numbers)
#     #print("Сумма чисел:", (numbers))
#
#     a = driver.find_element(By.CLASS_NAME, 'text').text
#     n = [int(num) for num in a.split()]
#     print(sum(n))
def suum2():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/3/3.html')
    p_elements = driver.find_elements(By.XPATH, "//div[@class='text']")

    total_sum = 0

    for p_element in p_elements:
        text = p_element.text
        numbers = [int(num) for num in text.split()]
        total_sum += sum(numbers)
    print("Общая сумма чисел из всех элементов:", total_sum)

def suum3():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/3/3.html')
    numbers = driver.find_elements(By.TAG_NAME, "p")
    res = 0
    for number in numbers:
        n = int(number.text)
        res += n
    print(res)