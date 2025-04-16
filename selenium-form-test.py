from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables
text_input = "Thosapol"
password_input = "Q48w94CE0Py"
textarea_input = "Selenium test form"
delay = 2  

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Input text input
wait.until(EC.presence_of_element_located((By.ID, "my-text-id"))).send_keys(text_input)
time.sleep(delay)

# Input password
driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[2]/input').send_keys(password_input)
time.sleep(delay)

# Input textarea
driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[3]/textarea').send_keys(textarea_input)
time.sleep(delay)

# Select Dropdown
Select(driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/label[1]/select')).select_by_value("2")
time.sleep(delay)

# Select Dropdown Datalist
driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/label[2]/input').send_keys("Bangkok")
time.sleep(delay)

# Upload file
file_path = "C:\\Users\\tytho\\Desktop\\test.txt" 
file_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/label[3]/input')
file_input.send_keys(file_path)
time.sleep(delay)

# Select Checkbox
checkbox1 = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/div[1]/label[1]/input')
if checkbox1.is_selected():
    checkbox1.click()
time.sleep(delay)

checkbox2 = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/div[1]/label[2]/input')
if not checkbox2.is_selected():
    checkbox2.click()
time.sleep(delay)

# Select Radio button
radio_button = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/div[3]/label/input')
radio_button.click()
time.sleep(delay)

# Select Color
color_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[3]/label[1]/input')
color_input.send_keys('#ff0000')
time.sleep(delay)

# Select date picker
date_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[3]/label[2]/input')
date_input.send_keys("2025-04-16")
time.sleep(1)
date_input.send_keys(Keys.ESCAPE)
time.sleep(delay)

# Example Range
range_slider = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[3]/label[3]/input')
driver.execute_script("arguments[0].value = 8;", range_slider)
driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", range_slider)
time.sleep(delay)

# Submit button
submit_button = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/button')
submit_button.click()
time.sleep(delay)

# Close browser
driver.quit()
