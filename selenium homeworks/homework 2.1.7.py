from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service('chromedriver.exe'), options=options)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get("https://suninjuly.github.io/get_attribute.html")
    time.sleep(1)
    treasure = driver.find_element(By.ID, 'treasure')
    valuex = int(treasure.get_attribute('valuex'))
    print(valuex)
    print(type(valuex))
    result = calc(valuex)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
except Exception as ex:
    print(ex)
    driver.close
    driver.quit
finally:
    print('Всё прошло успешно.')
    time.sleep(32)
