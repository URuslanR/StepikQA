from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(y):
    return math.log(abs(12*math.sin(x)))
    
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    
    browser.switch_to.window(browser.window_handles[1])
    
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(10)
    browser.quit()