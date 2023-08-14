from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")                    

#checking if element is selected
assert driver.find_element(By.ID,"displayed-text").is_displayed()
# then clicking on the hide button, again check if it is hidden properly
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
time.sleep(2)
assert not (driver.find_element(By.ID,"displayed-text").is_displayed())

