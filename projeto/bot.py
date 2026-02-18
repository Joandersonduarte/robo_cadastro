from selenium import webdriver as w
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time as t
import datetime as dt

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
servico = Service(ChromeDriverManager().install(), log_output=None)
servico = Service(ChromeDriverManager().install())
navegador = w.Chrome(service=servico, options=chrome_options)
wait = WebDriverWait(navegador, 5)