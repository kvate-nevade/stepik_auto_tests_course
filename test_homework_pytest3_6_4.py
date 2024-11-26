import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def answer():
    return str(math.log(int(time.time())))

@pytest.fixture(scope = 'session')
def load_config():
    with open('config.json', 'r') as cf:
        config = json.load(cf)
        return config



class TestLogin:
    @pytest.mark.parametrize('link_numbers', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_autorization(self, browser, load_config, link_numbers):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        link = f'https://stepik.org/lesson/{link_numbers}/step/1'
        browser.get(link)

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__auth_login'))).click()
        browser.find_element(By.NAME, 'login').send_keys(login)
        browser.find_element(By.NAME, 'password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
        
        time.sleep(4) # its necessary because stepik's servers is slow
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area'))).send_keys(answer())
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()
        time.sleep(4) # its necessary because stepik's servers is slow
        feedback_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text

        assert feedback_text == 'Correct!', f'The feedback text is not correct!, your result is {feedback_text}'


