import time

from selene import by, browser, be, have
from selene.support.shared.jquery_style import s

browser.config.timeout = 10

browser.open('https://victoretc.github.io/selenium_waits/')
browser.element('//*[@id="startTest"]').click()
s('#login').type('login')
s('#password').type('password')
s('#agree').click()
browser.element(by.text('Зарегистрироваться')).click()
s('#successMessage').should(have.text('Вы успешно зарегистрированы!'))
time.sleep(3)