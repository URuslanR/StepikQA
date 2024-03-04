from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math



link = "http://suninjuly.github.io/selects1.html"

def calc(num1, num2):
    return str(num1 + num2) 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    
    suma = calc(num1, num2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(suma) # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()        

    x = int(browser.find_element(By.ID, "input_value").text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла