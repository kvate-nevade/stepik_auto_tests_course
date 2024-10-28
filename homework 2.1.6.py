from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service('chromedriver.exe'), options=options)

try:
    driver.get("https://suninjuly.github.io/math.html")
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print(f'Value of people radio {people_checked}')
    assert people_checked is not None, "People radio is not selected by default"
except:
    print("Что-то пошло не так.")
    driver.close
    driver.quit