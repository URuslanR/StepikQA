from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser= webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc (x)
    
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    button.click()
    
finally:
    browser.quit()