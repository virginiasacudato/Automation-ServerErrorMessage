from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome('C:\\Users\\Maynar\\Desktop\\Automation-ServerErrorMessage\\driver\\chromedriver.exe',
                          options=chrome_options)

action = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(60)
driver.get(URL)



if driver.find_element("xpath", '//*[@id="divMensajesLogin"]'):
   print("element found!")





