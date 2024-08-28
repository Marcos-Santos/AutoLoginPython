# Program Auto-Login to Web Browser chrome
# Autor: Marcos Alexandre

import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# get the user's data from CSV file
with open ('Dados/Dados de Acesso.csv', 'r') as arq: 
        reader = csv.reader(arq)
        for line in reader:
                if ("Login:" in line):
                        user = line[1]
                if ("Password:" in line):
                       password = line[1]
           
# Open the Default Browser
print("iniciando parte dois")
#Toda vez ele vai verificar que versao esta sendo usado do seu Chrome e instalando o driver necessario 
#serv = Service(ChromeDriverManager().install())
#nav = webdriver.Chrome(service=serv)

navegador = webdriver.Chrome().get("www.google.com")
