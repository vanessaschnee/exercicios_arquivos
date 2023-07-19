#Extrair o nono e a quarta colunas do arquivo CSV sobre Região de influência das Cidades do IBGE
#Ignore a primeira linha que é cabeçalho.

import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print("baixando csv...")
        dados = entrada.read().decode('latin1')
        print("Dowload completo!")
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
