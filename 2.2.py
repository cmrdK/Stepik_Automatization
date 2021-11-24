from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sndk = browser.find_element(By.ID, "treasure")

    x = sndk.get_attribute("valuex")
    y = calc(x)
# Browser
    inputText = browser.find_element(By.ID, "answer")
    inputText.send_keys(y)
    checkBox1 = browser.find_element(By.ID, "robotCheckbox")
    checkBox1.click()
    radioButton1 = browser.find_element(By.ID, "robotsRule")
    radioButton1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    time.sleep(5)
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#