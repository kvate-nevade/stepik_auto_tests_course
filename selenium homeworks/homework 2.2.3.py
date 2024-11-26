from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome()
link = 'https://suninjuly.github.io/selects2.html'


try:
    driver.get(url = link)
    num_1 = driver.find_element(By.ID, 'num1').text
    num_2 = driver.find_element(By.ID, 'num2').text
    result = str(int(num_1) + int(num_2))
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(result)
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()

except Exception as ex:
    print(ex)

finally:
    sleep(32)
    driver.close()
    driver.quit()