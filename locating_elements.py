import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/client")
# By link Text
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"(//div/input)[1]").send_keys("sr@gmail.com")
driver.find_element(By.XPATH,"(//div/input)[2]").send_keys("123SC")
driver.find_element(By.ID,"confirmPassword").send_keys("123SC")
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
driver.minimize_window()
driver.maximize_window()
time.sleep(2)
driver.close()
driver.quit()
