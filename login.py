from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import json
import string

poster = json.loads(open("names.json").read())

class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password
    def signin(self):

        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")))
        uid.click()
        uid.send_keys(self.username)
        pswd = self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
        pswd.click()
        pswd.send_keys(self.password)
        btn = self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button")
        btn.click()
        time.sleep(3)
        for posta in poster["posts"]:
            self.driver.get(posta) 
            butn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")))
            butn.click()
            time.sleep(1)      
        self.driver.get("https://www.instagram.com/" + self.username)
        settings = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div > button")
        settings.click()
        logout = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div > button:nth-child(9)")))
        logout.click()
        time.sleep(1)
