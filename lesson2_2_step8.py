from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ruslan")
    browser.find_element(By.NAME, "lastname").send_keys("Yusupov")
    browser.find_element(By.NAME, "email").send_keys("mymail@mail.ru")
    button_path = browser.find_element(By.ID, "file")
   
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    button_path.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()  

finally:
    time.sleep(10)
    browser.quit()
