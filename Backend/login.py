from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login(driver):
    load_dotenv()
    user = os.getenv("email")
    password = os.getenv("password")
    your_username = os.getenv("your_username")

    try:
        driver.get("https://x.com/i/flow/login")
        # time.sleep(5)

        # Fetch all input fields by class name
        fields = driver.find_elements(By.CLASS_NAME, "r-30o5oe")
        
        # Input username
        username_field = fields[0]
        username_field.send_keys(user)
        username_field.send_keys(Keys.RETURN)
        # time.sleep(5)
        try:
            header = driver.find_element(By.ID, "modal-header").text
            if header == "Enter your phone number or username":
                username = driver.find_element(By.XPATH, "//input[@name='text']")
                username.send_keys(your_username)
                username.send_keys(Keys.RETURN)
                # time.sleep(5)
        except:
            pass

        # Input password
        fields = driver.find_elements(By.CLASS_NAME, "r-30o5oe")
        password_field = fields[1]
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        # time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")