from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from utils.browser import get_driver
from utils.file_handler import get_credentials

def login():
    driver = get_driver()
    credentials = get_credentials()
    
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    email_field.send_keys(credentials["email"])
    password_field.send_keys(credentials["password"])
    password_field.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for login to complete
    print("Logged in successfully")
    return driver

if __name__ == "__main__":
    driver = login()
    driver.quit()
