import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_register_1():

    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys("Kirill")
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys("Anoshko")
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys("akw98@ya.ru")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == 'Congratulations! You have successfully registered!', 'The text of the successful registration must meet the expectation'



def test_register_2():
    
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys("Kirill")
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys("Anoshko")
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys("akw98@ya.ru")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == 'Congratulations! You have successfully registered!', 'The text of the successful registration must meet the expectation'


if __name__ == '__main__':
    pytest.main()
    print("Everything passed")