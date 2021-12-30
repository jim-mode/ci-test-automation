from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=800,640')

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://google.com/')
screenshot = driver.save_screenshot('google_home.png')
driver.quit()
