from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Name")
    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Last name")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'upload.txt')  # добавляем к этому пути имя файла
    fileup = browser.find_element(By.NAME, "file")
    fileup.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#