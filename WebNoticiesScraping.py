from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


driver =  webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.mercadolibre.com.co/")
driver.close()