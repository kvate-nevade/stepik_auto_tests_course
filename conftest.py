import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    

@pytest.fixture(scope = 'function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None

    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(10)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError('--browser_name shouild be chrome or firefox')
    
    yield browser  # Объект браузера передается в тест

    print('\nbrowser is quiting..')
    browser.quit()
