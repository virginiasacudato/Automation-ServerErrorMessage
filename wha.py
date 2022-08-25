from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")
PHONE = os.environ.get("PHONE")

client = requests.Session()
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument(
    f"user-data-dir=C:\\Users\\Maynar\\Desktop\\Automation-ServerErrorMessage\\sessions\\54{PHONE}\\")

driver = webdriver.Chrome('C:\\Users\\Maynar\\Desktop\\Automation-ServerErrorMessage\\driver\\chromedriver.exe',
                          chrome_options=chrome_options)
count = 0


data = [
    {"_to": "Virginia Sacudato", "_message": "Prueba 1"},
    # {"_to": "xxxxxxxxx", "_message": "Prueba 1"},
    # {"_to": "xxxxxxxx", "_message": "Prueba 1"}
]  

driver.get(URL)


username_login = driver.find_element("xpath", '//*[@id="Usuario"]')
username_login.click()
time.sleep(5)
username_login.send_keys("admin")


password_login = driver.find_element("xpath", '//*[@id="Password"]')
password_login.click()
password_login.send_keys("admin")
time.sleep(3)

button_ingresar = driver.find_element("xpath", '//*[@id="btnIngresar"]')
button_ingresar.click()
time.sleep(5)

mensaje_de_error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divMensajesLogin"]')))
print(mensaje_de_error)

if WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divMensajesLogin"]'))):
#if driver.find_element("xpath", '//*[@id="divMensajesLogin"]'):
   print("Elemento encontrado! Reporte iniciado.")
   time.sleep(10)
   #driver.close()
   driver.get(f"https://web.whatsapp.com/send?phone=xxxxxxxx")
   for i in data:
    time.sleep(2)
    wait = WebDriverWait(driver, 600)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    try:
        time.sleep(15)
        group_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p3_M1")))
        group_title.send_keys(i["_message"])
        time.sleep(2)
        group_titles = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
        group_titles.click()
        time.sleep(5)
        print("Notificación enviada.")
    except Exception as e:
        print(e)
        pass
    driver.close()
else: 
    print("Elemento no encontrado")