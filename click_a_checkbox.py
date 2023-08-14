import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Sravya")
driver.find_element(By.NAME,"email").send_keys("se@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Kvmkvm")
# checkbox, click(): clicks the checkbox
driver.find_element(By.ID,"exampleCheck1").click()
driver.maximize_window()
# submit button using xpath
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
# to check if the success message is correct or not , and instead of using xpath , we are using css selectopr just for fun
message = driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
assert "Success!" in message
time.sleep(3)
driver.close()
