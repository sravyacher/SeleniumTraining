from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# selecting third radio button
driver.find_elements(By.NAME,"radioButton")[2].click()
time.sleep(2)