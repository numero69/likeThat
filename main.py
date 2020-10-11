from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import json
import string
import time
import login
username = json.loads(open("names.json").read())
driver = 0

def main():
    global driver
    print("running script")
    #change the path to your chromedrived executable
    driver = webdriver.Chrome("PATH")
    for name in username["accounts"]:
        print("running with %s and %s" % (name["username"], name["password"]))
        l = login.Login(driver, name["username"], name["password"])
        l.signin() 
        
    

                 
           
    
     
if __name__ == "__main__":
    main()

