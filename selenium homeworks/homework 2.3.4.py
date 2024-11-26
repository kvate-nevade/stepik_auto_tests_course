from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

driver = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'


try:
    driver.get(url = link)
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
    driver.switch_to.alert.accept()
    sleep(1)
    x = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
    
except Exception as ex:
    print(ex)

finally:
    sleep(32)
    driver.close
    driver.quit