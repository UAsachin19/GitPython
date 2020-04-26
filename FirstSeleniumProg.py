from selenium import webdriver

##driver = webdriver.Chrome(executable_path="D:\\Softwares\\Python\\ChromeDriver\\chromedriver.exe")
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="D:\\Softwares\\Python\\GeckoDriver\\geckodriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Sachin")

driver.find_element_by_css_selector("input[name='email']").send_keys("js@gmail.com")

driver.find_element_by_xpath("//input[@placeholder = 'Password']").send_keys("Hello")

driver.find_element_by_css_selector("#exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_value("Male")
dropdown.select_by_visible_text("Female")

driver.find_element_by_css_selector("input[class*='btn-success']").click()

print(driver.find_element_by_css_selector("div[class*='alert-success']").text)

driver.close()

