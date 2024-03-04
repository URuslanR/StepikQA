from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(y):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)
    
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    
    browser.find_element(By.ID, 'answer').send_keys(y)
    
    browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(5)
    browser.quit()
