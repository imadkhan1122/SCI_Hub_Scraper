import undetected_chromedriver as uc
from selenium import webdriver
import urllib
import requests
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

def GET_PAPER(str_):   
    URL = 'https://sci-hub.hkvisa.net/'
    name = ''
    options = Options()
    # prefs = {"profile.default_content_setting_values.geolocation" :2}
    # options.add_experimental_option("prefs",prefs)
    options.add_argument('--headless')
    # open chrome browser
    driver = driver = uc.Chrome(options=options)
    # Go to given URL
    driver.get(URL)
    # wait for 5 seconds
    delay = 10 # seconds
    openbtn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'open')))
    while openbtn.text != 'open':
        openbtn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'open')))
    try:
        # locate searchbar and type product name
        SearchBar = driver.find_element(By.CSS_SELECTOR, 'input[type="textbox"]')
        SearchBar.send_keys(str(str_) + Keys.RETURN)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'sci')))
        PDF_Link = driver.find_element(By.ID, 'article')
        PDF_URL = PDF_Link.find_element(By.ID, 'pdf')
        Link = PDF_URL.get_attribute('src')
        Link = Link.replace('#view=FitH', '')
        _, name = os.path.split(Link)
        r = requests.get(Link)
        while r.status_code != 200:
            r = requests.get(Link)
    except:
        print(driver.find_element(By.TAG_NAME, 'Body').text)
    driver.quit()
    return name
    