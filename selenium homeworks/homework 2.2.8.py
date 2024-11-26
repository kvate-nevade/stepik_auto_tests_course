from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'

fname = 'Kirill'
lname = 'Anoshko'
email = 'akw98@ya.ru'
file_directory = r'C:\Users\Kira\Downloads\sandbox.txt'


try:
    driver.get(url = link)
    driver.find_element(By.NAME, 'firstname').send_keys(fname)
    driver.find_element(By.NAME, 'lastname').send_keys(lname)
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'file').send_keys(file_directory)
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()

except Exception as ex:
    print(ex)

finally:
    sleep(30)
    driver.close
    driver.quit
