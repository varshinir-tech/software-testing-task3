from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Maximize Window
driver.maximize_window()

# -------------------------------
# Test Case 1: Positive Login Test
# -------------------------------

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("student")
password.send_keys("Password123")

driver.find_element(By.ID, "submit").click()

time.sleep(20)

if "logged-in-successfully" in driver.current_url:
    print("Positive Login Test Passed")

driver.back()

time.sleep(20)

# -------------------------------
# Test Case 2: Invalid Username
# -------------------------------

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("wrongUser")
password.send_keys("Password123")

driver.find_element(By.ID, "submit").click()

time.sleep(2)

error = driver.find_element(By.ID, "error")

if error.is_displayed():
    print("Invalid Username Test Passed")

driver.refresh()

time.sleep(20)

# -------------------------------
# Test Case 3: Invalid Password
# -------------------------------

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("student")
password.send_keys("wrongPassword")

driver.find_element(By.ID, "submit").click()

time.sleep(20)

error = driver.find_element(By.ID, "error")

if error.is_displayed():
    print("Invalid Password Test Passed")

driver.refresh()

time.sleep(20)

# -------------------------------
# Test Case 4: Empty Fields Test
# -------------------------------

driver.find_element(By.ID, "submit").click()

time.sleep(120)

current_url = driver.current_url

if "practice-test-login" in current_url:
    print("Empty Fields Test Passed")

# Close Browser
time.sleep(20)
driver.quit()