
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC

# url = 'https://parsinger.ru/methods/1/index.html'
#
# driver = webdriver.Chrome()
# try:
#     for i in range(100):
#         driver.get(url)
#         driver.refresh()
#         if i == driver.find_element((By.ID, 'result')):
#             print("Элемент 'result' найден:", a.text)
# finally:
#     driver.quit()


from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://parsinger.ru/methods/1/index.html'

driver = webdriver.Chrome()
try:
    for i in range(100):
        driver.get(url)
        driver.refresh()
        result_element = driver.find_element(By.ID, 'result')
        result_text = result_element.text
        if str(i) == result_text:
            print("Элемент 'result' найден:", result_text)
            break
finally:
    driver.quit()
