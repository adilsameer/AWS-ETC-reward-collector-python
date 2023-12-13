import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
import os


# AWS ETC login url
LOGIN_URL = "https://aws-emergingtalent.influitive.com/users/sign_in"

# Enter your credentials below between "" quotes
# # NOTE: You can also use environment variables for your credentials
USER_EMAIL = "user@example.com"
USER_PASSWORD = "password#1234"

# This login funtion use your credentials to login on AWS ETC page
def login():
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")
    email_input.send_keys(USER_EMAIL)
    password_input.send_keys(USER_PASSWORD)
    sign_in_btn = driver.find_element(By.ID, "sign-in-button")
    sign_in_btn.send_keys(Keys.ENTER)

# collect reward funtion is run after login with your credentials and collect reward
def collect_reward():
    try:
        reward = driver.find_element(By.CSS_SELECTOR, ".css-w09zei button")
        reward.click()
    except:
        print("Reward already collected")


currect_time = dt.now()

# While loop is used to run program always
while True:
    # if condition check for current time to be 24 hour (12 AM)
    if currect_time.hour == 0:
        # random minutes choose random minute between 1 minute to 60 minutes
        random_minutes = random.randint(60, 3600)
        # program stops for random minutes
        time.sleep(random_minutes)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Driver open webpage
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)
        login()
        # After login to waits for page to load then collect reward
        time.sleep(10)
        collect_reward()
        # After collecting reward it close chrome
        driver.quit()
        # Program sleeps for again 24 hours and rerun after 24  hours
        sleep_24_hours = 86400 - random_minutes - 10
        time.sleep(sleep_24_hours)





