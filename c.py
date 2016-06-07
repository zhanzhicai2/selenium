from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.maiziedu.com/")
ele = browser.find_element_by_css_selector('img[alt = "UI设计"]')
ele.click()