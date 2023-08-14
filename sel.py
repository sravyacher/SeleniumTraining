from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get("https://chat.openai.com/c/b79528c4-3cd0-4f84-ab3a-cd52d9421b81")
time.sleep(3)
driver.close()