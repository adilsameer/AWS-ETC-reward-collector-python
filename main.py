import time
from selenium.common import TimeoutException
from bot import Autobot
import os

# Demo https://replit.com/@AdilSameer/amazon-etc-auto-reward-collector-python
# Github https://github.com/adilsameer/AWS-ETC-reward-collector-python

# Enter your credentials below between "" quotes
USER_EMAIL = "user@example.com"
USER_PASSWORD = "pass@123"
# # NOTE: You can also use environment variables for your credentials like below for Windows
# USER_EMAIL = os.environ["AWS_EMAIL"]
# USER_PASSWORD = os.environ["AWS_PASSWORD"]
# And for replit environment variables (Secrets) use
# USER_EMAIL = os.getenv("AWS_EMAIL")
# USER_PASSWORD = os.getenv("AWS_PASSWORD")

initial_time = time.time()
keep_running = True
while keep_running:
    bot = Autobot()
    try:
        bot.user_login(USER_EMAIL, USER_PASSWORD)
    except TimeoutException:
        print("Invalid credentials")
        bot.quit()
        break
    else:
        bot.reward_collect()
        bot.quit()
        time_after_execution = time.time()
        time_difference = time_after_execution - initial_time
        remaining_time_to_wait = 24 * 60 * 60 - time_difference
        time.sleep(remaining_time_to_wait)

# Points collection from challenges(Tasks) is under testing
