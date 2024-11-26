from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

driver = webdriver.Chrome()

link = 'https://SunInJuly.github.io/execute_script.html'


try:
    driver.get(url = link)
    x = driver.find_element(By.ID, 'input_value').text
    result = math.log(abs(12*math.sin(int(x))))
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'robotCheckbox').click()

    button = driver.find_element(By.CSS_SELECTOR, '.form-check-label[for="robotsRule"]')
    driver.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

except Exception as ex:
    print(ex)

finally:
    sleep(32)
    driver.close()
    driver.quit()