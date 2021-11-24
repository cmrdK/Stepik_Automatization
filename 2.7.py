from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser=webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    alert1 = browser.switch_to.alert
    alert1.accept()

    x_e = browser.find_element(By.ID, "input_value")
    y = str(math.log(abs(12*math.sin(int(x_e.text)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

#