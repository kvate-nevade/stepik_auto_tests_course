from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url=link)
    x = browser.find_element(By.ID, 'answer').text
    result = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(result)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()

except Exception as ex:
    print(ex)
    pass

finally:
    time.sleep(35)
    browser.close()
    browser.quit()