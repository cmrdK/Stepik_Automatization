from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("document.title='ROBOTS RULE';alert('Robots at work. HAHAHAHA');")