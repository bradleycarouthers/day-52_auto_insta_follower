from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random
import secret

CHROME_DRIVER_PATH = "C:/Development/chromedriver_win32/chromedriver.exe"
ACCOUNT = secret.ACCOUNT
EMAIL = secret.EMAIL
PASSWORD = secret.PASSWORD


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(EMAIL)
        pass_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)

    def find_follower(self):
        time.sleep(10)
        self.driver.get(url=f"https://www.instagram.com/{ACCOUNT}")

        time.sleep(3)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(3)

    def follow(self):
        random_time = random.randint(4, 14)

        all_buttons = self.driver.find_elements_by_css_selector(".PZuss li button")
        try:
            for i in range(0, len(all_buttons)):
                all_buttons[i].click()
                time.sleep(random_time)
        except ElementClickInterceptedException:
            cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            cancel.click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
