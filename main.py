from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.saucedemo.com")
print('Application title is: ', driver.title)
print('Application URL is: ', driver.current_url)
try:
  WebDriverWait(driver, 3)
  time.sleep(3)
finally:
  driver.quit()