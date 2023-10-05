from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://casenik.com.ua/user/login")

email_field = driver.find_element(By.XPATH, '//input[@id="email"]')
email_field.send_keys("test8@example.com")
password_field = driver.find_element(By.XPATH, '//input[@id="pasword"]')
password_field.send_keys("test1234567890")
login_button = driver.find_element(By.XPATH, '//button[@class="btn button-gen"]')
login_button.click()

message = WebDriverWait(driver, 29).until_not(
    #EC.element_to_be_clickable(By.XPATH, "//div[@class='alert alert-success']"))
    EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))
#явне очікування доки елемент не зникне - until not
# явне очікування доки елемент з'явиться - until
time.sleep(5)


