from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    y = str(abs(math.log(12*math.sin(int(x.text)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()

#