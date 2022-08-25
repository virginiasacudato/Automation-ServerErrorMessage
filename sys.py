from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pywhatkit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from os.path import join, dirname
from dotenv import load_dotenv


contact = "Virginia Sacudato"
text = "PRUEBA 1 SELENIUM"

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("URL")


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


driver = webdriver.Chrome('C:\\Users\\Maynar\\Desktop\\Automation-ServerErrorMessage\\driver\\chromedriver.exe',
                          options=chrome_options)

action = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(60)
driver.get(URL)



if driver.find_element("xpath", '//*[@id="divMensajesLogin"]'):
   print("Elemento encontrado! Reporte iniciado.")

# //*[@id="side"]/div[1]/div/div/div[2]/div
   time.sleep(10)
   driver.get("https://web.whatsapp.com")
   print("Scan QR Code, And then Enter")
   input()
   print("Logged In")
   inp_xpath_search = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
   input_box_search = WebDriverWait(driver,30).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   input_box_search.click()
   print("Elemento de busqueda clickeado")
   time.sleep(2)
   input_box_search.send_keys(contact)
   time.sleep(2)
   selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
   selected_contact.click()
   inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
   input_box = driver.find_element_by_xpath(inp_xpath)
   time.sleep(2)
   input_box.send_keys(text + Keys.ENTER)
   time.sleep(2)
   driver.quit()

else: 
   print ("No se encontró el elemento, todo correcto!")




