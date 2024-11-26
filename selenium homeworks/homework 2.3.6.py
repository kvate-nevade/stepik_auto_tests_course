from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

driver = webdriver.Chrome()

link = 'http://suninjuly.github.io/redirect_accept.html'


try:
    driver.fullscreen_window
    driver.get(url = link)
    driver.find_element(By.CSS_SELECTOR, 'button[class="trollface btn btn-primary"]').click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element(By.ID, 'input_value').text
    print(x)
    driver.find_element(By.ID, 'answer').send_keys(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()

except Exception as ex:
    print(ex)

finally:
    sleep(20)
    driver.close
    driver.quit