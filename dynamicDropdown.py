import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="D:\\Softwares\\Python\\GeckoDriver\\geckodriver.exe")

driver.get("https://www.makemytrip.com/")

driver.find_element_by_css_selector("label[for='fromCity'] input").click()

driver.find_element_by_css_selector("input[placeholder='From']").send_keys("Del")

time.sleep(2)

print(driver.find_elements_by_css_selector("p[class*='blackText']"))
