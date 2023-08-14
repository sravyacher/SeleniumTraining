import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH,"").click()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for ch in checkboxes:
    if ch.get_attribute("value") == "option2":
        ch.click()
        assert ch.is_selected() # asserting i.e checking if the checkbox is checked or not
        break
time.sleep(2)