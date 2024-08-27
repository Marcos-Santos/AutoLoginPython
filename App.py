# Program Auto-Login to Web Browser chrome
# Autor: Marcos Alexandre

import csv

print("Inicio programa")

with open ('Dados/Dados de Acesso.csv', 'r') as arq: 
        leitor = csv.reader(arq)
        for linha in leitor:
            print(linha)

print("Teste de uso dos Dados")
print(linha[0])
print(linha[1])


