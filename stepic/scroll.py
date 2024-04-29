import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


def scroll():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        browser.execute_script("window.scrollBy(0,5000)")
        height = browser.execute_script("return document.body.scrollHeight")
        height1 = browser.execute_script("return window.innerHeight")
        print(f'Высота {height}')
        print(f'Ширина {height1}')
#scroll()

def scroll1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)
        time.sleep(3)
#scroll1()

def scroll2():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        tags_input = browser.find_elements(By.TAG_NAME, 'input')

        for input in tags_input:
            input.send_keys(Keys.DOWN)
            time.sleep(0)
#scroll2()

def scroll3():
    with webdriver.Chrome() as browser:
        browser.get(r"https://parsinger.ru/selenium/5.7/3/index.html")

        list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
        while True:  # Начинаем бесконечный цикл

            # Ищем все элементы input на веб-странице и добавляем их в список input_tags
            input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

            # Обходим каждый элемент input в списке
            for tag_input in input_tags:
                # Проверяем, не обрабатывали ли мы уже этот элемент ранее
                if tag_input not in list_input:
                    tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                    browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                    tag_input.click()  # Кликаем на элемент
                    time.sleep(.1)
                    list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов
#scroll3()

def action():
    driver = webdriver.Chrome()
    driver.get("https://parsinger.ru/selenium/5.7/2/index.html")
    draggable = driver.find_element(By.ID, "draggable")# Найти элемент на странице с использованием локатора By
    actions = ActionChains(driver)# Использование ActionChains для выполнения перетаскивания элемента
    time.sleep(2)
    actions.drag_and_drop_by_offset(draggable, -100, 0).perform()# 1. Переместить блок влево на 100px
    time.sleep(2)
    actions.drag_and_drop_by_offset(draggable, 0, 100).perform()# 2. Переместить блок вниз на 100px
    actions.drag_and_drop_by_offset(draggable, 100, 0).perform()# 3. Переместить блок вправо на 100px
    actions.drag_and_drop_by_offset(draggable, 0, -100).perform()# 4. Переместить блок вверх на 100px
    driver.quit()# Закрыть браузер после завершения
action()