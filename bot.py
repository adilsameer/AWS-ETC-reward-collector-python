from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://aws-emergingtalent.influitive.com/users/sign_in"


class Autobot:

    def __init__(self):
        self.driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension('captcha_solver_extension.crx')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        # self.chrome_options.add_argument('headless')
        # self.chrome_options.add_experimental_option("detach", True)

    def user_login(self, email, password):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        url_wait = WebDriverWait(self.driver, timeout=60)
        self.driver.get(LOGIN_URL)
        email_input = self.driver.find_element(By.NAME, "user[email]")
        password_input = self.driver.find_element(By.NAME, "user[password]")
        email_input.send_keys(email)
        password_input.send_keys(password)
        sign_in_btn = self.driver.find_element(By.ID, "sign-in-button")
        sign_in_btn.click()
        url_wait.until(EC.url_changes(LOGIN_URL))

    def reward_collect(self):
        try:
            reward_wait = WebDriverWait(self.driver, timeout=15)
            reward = (By.CSS_SELECTOR, ".css-w09zei button")
            reward_btn = reward_wait.until(EC.visibility_of_element_located(reward))
            reward_btn.click()
        except:
            print("Reward already collected")

    def quit(self):
        self.driver.quit()
