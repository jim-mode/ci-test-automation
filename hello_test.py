import allure
import pytest
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.feature('Feature1')
@allure.story('Story1')
def test_capitalize_string_01():
    assert capitalize_string('test') == 'Test'

@allure.feature('Feature2')
@allure.story('Story2', 'Story3')
@allure.story('Story4')
class TestCap:
    def test_capitalize_string_02(self):
        assert capitalize_string('python') == 'Python'

@allure.feature('Feature3')
@pytest.mark.fruits
def test_capitalize_string_03():
    assert capitalize_string('apple') != 'Pear'

@allure.feature('Random Fail')
def test_random_fail():
    assert randint(0,1) == 1

@allure.feature('Selenium with Chrome')
@allure.story('Story4')
@pytest.mark.web
def test_selenium():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=800,640')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('http://google.com/')
    assert "Google" == driver.title
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('mode transportation')
    search_box.submit()
    screenshot = driver.save_screenshot('google_search.png')
    assert "MODE Transportation" in driver.page_source
    assert "Latest Lottery Number" not in driver.page_source

    driver.close()
    driver.quit()

@allure.feature('Selenium with Chrome User Agent')
@allure.story('Story5')
@pytest.mark.web
def test_selenium():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=800,640')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (MY AWSOME USER AGENT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('http://whatsmyuseragent.org/')
    screenshot = driver.save_screenshot('user_agent.png')
    assert "MY AWSOME USER AGENT" in driver.page_source

    driver.close()
    driver.quit()

def capitalize_string(s):
  if not isinstance(s, str):
    raise TypeError('Please provide a string')
  return s.capitalize()
