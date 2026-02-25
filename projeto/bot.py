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

delay = t.sleep(1)

def leitura_dados():
     try:
          df = pd.read_excel('/home/joanderson/Área de trabalho/Projetos/robo_cadastro/challenge.xlsx')
          print('Dados lidos com sucesso.')
          return df
     except FileNotFoundError:
          print('Arquivo não encontrado.')
          return None

def login():
    try:
        navegador.get('https://rpachallenge.com/')
        navegador.maximize_window()
        print('Acessando site.')
    except TimeoutError:
            navegador.refresh()
            print('Tempo de carregamento excedido. Tentando novamente...')
    except Exception as e:
        navegador.quit()
        print('Ocorreu um erro inesperado: ', e)

def start_boot():
    dados = leitura_dados()
    
    for index, row in dados.iterrows():
        nome = row['First Name']
        sobrenome = row['Last Name ']
        companhia = row['Company Name']
        cargo = row['Role in Company']
        endereco = row['Address']
        email = row['Email']
        fone = row['Phone Number']

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]'))).send_keys(cargo)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]'))).send_keys(nome)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]'))).send_keys(companhia)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]'))).send_keys(endereco)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]'))).send_keys(email)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]'))).send_keys(fone)
        delay
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]'))).send_keys(sobrenome)
        delay 
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click() 
        print(f'Cadastro de {nome} {sobrenome} realizado com sucesso.')
    print('Todos os cadastros foram realizados com sucesso.')
    t.sleep(5)

if __name__ == '__main__':
    print('Bot iniciando às: ', dt.datetime.now().strftime('%H:%M:%S'))
    login()
    print('Iniciando cadastro dos usuários às: ', dt.datetime.now().strftime('%H:%M:%S'))
    start_boot()
    print('Bot finalizado às: ', dt.datetime.now().strftime('%H:%M:%S'))
