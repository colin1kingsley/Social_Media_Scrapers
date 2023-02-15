from selenium import webdriver
import os
import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# c.f. Note 1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#

class InstagramBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag

        # c.f. Note 1
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #

        self.by = By
        self.ec = EC
        self.webDriverWait = WebDriverWait

        time.sleep(2)
        self.login()
        time.sleep(5)
        self.explore_hashtags()
        # self.explore_reels()
        # self.like_reel()
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")


        self.webDriverWait(self.driver, 25).until(self.ec.presence_of_element_located((self.by.NAME, 'username')))
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.NAME, 'password')))

        self.driver.find_element('name','username').send_keys(self.username)
        self.driver.find_element('name', 'password').send_keys(self.password)

        self.webDriverWait(self.driver, 20).until(self.ec.element_to_be_clickable((self.by.XPATH, '//*[contains(text(), "Log in")]')))
        self.driver.find_element('xpath', '//*[contains(text(), "Log in")]').click()

    def explore_hashtags(self):
        print(type(self.driver.get('https://www.instagram.com/explore/tags/' + self.hashtag)))
        time.sleep(10)

    def explore_reels(self):
        self.driver.get('https://www.instagram.com/reels/videos')
    
    def like_reel(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'button._abl-._abm2').click()

    def get_hashtags(self):
        self.driver.find_element(By.CSS_SELECTOR, 'h1._aacl._aaco._aacu._aacx._aad7._aade').click()
        


# this is just the log

username = "" # <put your username here> #
password = "" # <put your password here> #
tags = "" # <put your tags here> #
hashtag = "cars"

ig = InstagramBot(username, password, hashtag)


