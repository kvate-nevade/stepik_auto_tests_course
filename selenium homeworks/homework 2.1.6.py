from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")

    print(f'Value of people radio {people_checked}')
    assert people_checked is not None, "People radio is not selected by default"

except:
    print("Что-то пошло не так.")

finally:
    browser.close
    browser.quit