# Dynamic dropdown : which change according to eitehr what is searched in the search box, what is choosen etc
# Basically dropdown which is affected  by action on another element
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By



driver = webdriver.Edge()

driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
# now , since it is a dynamic list , we have no gaurentee, 'India' which appeared on the 2nd element, will appera at the same place for the next search
# Hence , we need to test if the elment which has text "India" is selected  
# First we will have a list whcih will contain all the elements which will appear on the dropdown list
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))
for c in countries:
    if c.text == "India":
        c.click()
# DOUBT