from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Фукция сокращения кода
def findBySelector(selector, value):
    return browser.find_element_by_css_selector('[' + selector + '="' + value + '"]')

# Цикл, который позволяет выбрать количество нужных КТ
def fillCallCard(count):
    i = 0
    while i <= count:
        browser.find_element_by_id("main_kt_reason_chosen").click()
        findBySelector('data-option-array-index', '1').click()
        browser.find_element_by_id("kt-register-button").click()
        i = i + 1
        time.sleep(2)

try: 
    link = "http"
    browser = webdriver.Chrome()
    browser.get(link)

    # Разворачиваем браузер на полный экран
    browser.maximize_window()

    # Уменьшаем зум страницы ()
    # browser.execute_script("document.body.style.zoom = '75%'")

    # Авторизация в системе (логин + пароль + ввод)
    login = findBySelector('name', 'login').send_keys('')
    password = findBySelector('name', 'password').send_keys('')
    send = browser.find_element_by_class_name('btn-footer').click()

    # Нажимаем кнопку "Новый вызов"
    newСall = findBySelector('title', 'alt+1').click()

    # Выбираем повод к вызову, регистрируем КТ (в скобках: количество КТ+1)
    fillCallCard(3)

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # Закрываем браузер после всех манипуляций
    browser.quit()
