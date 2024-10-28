from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service('chromedriver.exe'), options=options)

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver.get(url=link)
    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)
    driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys(result)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()

except Exception as ex:
    print(ex)
    pass

finally:
    time.sleep(35)
    driver.close()
    driver.quit()