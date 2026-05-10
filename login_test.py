from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("student")
password.send_keys("Password123")

driver.find_element(By.ID, "submit").click()

time.sleep(190)

driver.quit()