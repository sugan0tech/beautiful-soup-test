from selenium import webdriver
import cv2
import pytesseract
chrome_driver_path = "geckodriver"
driver = webdriver.Firefox(executable_path=chrome_driver_path)
url = "https://aishe.gov.in/aishe/home"
driver.get(url=url)
EMAIL = "nvinishah@gmail.com"
PASSWORD = "Aishe@1234"
login = driver.find_element("xpath", "/html/body/header/div/div/div[1]/ul/li[3]/a")
login.click()
email_id = driver.find_element("id", "emailId")
email_id.send_keys(EMAIL)
password = driver.find_element("id", "password")
password.send_keys(PASSWORD)

res_img = driver.find_element_by_css_selector('[alt="login"]')
res_img.save_screenshot("screen.png")
