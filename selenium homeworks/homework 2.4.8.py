from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin

driver = webdriver.Chrome()
driver.implicitly_wait(5)

link = 'http://suninjuly.github.io/explicit_wait2.html'


try:
    driver.get(link)
    WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    x = int(driver.find_element(By.ID, 'input_value').text)
    result = log(abs(12*sin(x)))
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'solve').click()

except Exception as ex:
    print(ex)

finally:
    sleep(100)
    driver.close()
    driver.quit()