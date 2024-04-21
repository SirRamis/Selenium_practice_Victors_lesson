from selenium import webdriver


def met_5_6_3():
    url = 'https://parsinger.ru/methods/3/index.html'
    driver = webdriver.Chrome()
    driver.get(url)
    cookies = driver.get_cookies()

    for cookie in cookies:
        a = cookie['name']
        b = a.split('_')
        if len(b) >= 3:  # Проверяем, что в списке достаточно элементов
            third_element = b[2]  # Получаем третий элемент списка b
            try:
                third_element_int = int(third_element)  # Преобразуем его в целое число
                if third_element_int % 2 == 0:
                    print(f"Число {third_element_int} четное.")
                else:
                    print(f"Число {third_element_int} нечетное.")
            except ValueError:
                print("Ошибка: Невозможно преобразовать в целое число.")
met_5_6_3()