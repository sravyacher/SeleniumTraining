import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
# This is code to handle static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(3)
dropdown.select_by_visible_text("Male")
