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
#suum3()
def suum4():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/3/3.html')
    numbers = driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    res = 0
    for number in numbers:
        n = int(number.text)
        res += n
    print(res)
#suum4()

def checkbox():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/4/4.html')
    checks = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/input")
    for check in checks:
        check.click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/input').click()
    print(driver.find_element(By.ID, "result").text)
#checkbox()

def check_val():
    numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
               39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
               74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
               119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
               154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
               187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
               208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
               234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
               256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
               292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
               318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
               353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
               419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
               452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
               480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/5/5.html')

    checks = driver.find_elements(By.CLASS_NAME, 'check')
    btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/input')
    for i in checks:
        a = int(i.get_attribute('value'))
        if a in numbers:
            i.click()
    btn.click()
    print(driver.find_element(By.ID, "result").text)
#check_val()

def ch_list():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/7/7.html')
    q = driver.find_elements(By.TAG_NAME, 'option')
    btn = (By.XPATH, '//*[@id="input_result"]')
    btn1 = (By.XPATH, '//*[@id="sendbutton"]')

    t = 0
    for i in q:
        a = int(i.text)
        t += a
    print(t)
    driver.find_element(*btn).send_keys(t)
    time.sleep(3)
    driver.find_element(*btn1).click()
    time.sleep(3)
    print(driver.find_element(By.ID, "result").text)

#ch_list()

def ch_list3():
    driver = webdriver.Chrome()
    driver.get('https://parsinger.ru/selenium/6/6.html')
    arg = (12434107696 * 3 * 2) + 1
    print(arg)
    dropdown = driver.find_element(By.ID, 'selectId') # Найти выпадающий список
    dropdown.click()  # Нажать на выпадающий список, чтобы отобразить опции
    time.sleep(3)
    options = driver.find_elements(By.TAG_NAME, 'option') # Найти все опции в выпадающем списке
    for option in options: # Пройтись по всем опциям и найти нужную
        if option.text == str(arg):  # Проверяем, соответствует ли текст опции значению arg
            option.click()  # Кликаем на найденную опцию
            time.sleep(3)
            break  # Прерываем цикл, так как нужная опция уже найдена
    send_button = driver.find_element(By.ID, 'sendbutton') # Найти кнопку "Отправить" и кликнуть на нее
    send_button.click()
    time.sleep(3)
    print(driver.find_element(By.ID, "result").text)
#ch_list3()

from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)

    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.TAG_NAME, 'a')

    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))