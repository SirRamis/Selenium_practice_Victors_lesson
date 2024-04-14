import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Добавляем импорт

# Создаем экземпляр драйвера Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1440,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Загружаем веб-страницу, на которой нужно выполнить перетаскивание
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

# Переключаемся на iframe, где расположен перетаскиваемый объект
iframe = driver.find_element(By.XPATH, '//*[@id="content"]/iframe')
driver.switch_to.frame(iframe)
time.sleep(3)

# Находим элементы, которые нужно перетащить и куда их нужно перетащить
source_element = driver.find_element(By.XPATH, '//*[@id="draggable"]/p')
target_element = driver.find_element(By.XPATH, '//*[@id="droppable"]')
time.sleep(3)

# Создаем экземпляр ActionChains и выполняем перетаскивание
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()
time.sleep(3)

# Закрываем драйвер
driver.quit()
