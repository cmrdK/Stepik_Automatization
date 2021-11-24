import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time
import math

try:
    browser = webdriver.Chrome()
   # browser.implicitly_wait(13)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    but1 = browser.find_element(By.ID, "book")
    text = WebDriverWait(browser, 13).until(
        ES.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    but1.click()

    x = browser.find_element(By.ID, "input_value")
    y = str(abs(math.log(12*math.sin(int(x.text)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.ID, "solve")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
#
