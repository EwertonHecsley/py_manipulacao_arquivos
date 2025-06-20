import os
import shutil
from pathlib import Path

#Pega o caminho relativo da pasta onde o script está localizado.
ROOT_PATH = Path(__file__).parent

#Comando para criar um nvo diretório dentro do caminho especificado.
os.mkdir(ROOT_PATH / 'novo_diretorio')

#Comando para "escrever" ("W") criar um arquivo de um diretório para outro.
try:
    with open(ROOT_PATH / 'novo_diretorio' / 'arquivo.txt', 'w',encoding='utf-8') as arquivo:
        arquivo.write('Este é um arquivo criado com Python.\n')
        arquivo.write('Estamos aprendendo a manipular arquivos e diretórios.\n')
except IOError as err:
        print(f'Ocorreu um erro ao criar o arquivo: {err}')    


#Alterar nome do arquivo
os.rename(ROOT_PATH/'novo_diretorio'/'arquivo.txt', ROOT_PATH/'novo_diretorio'/'arquivo_alterado.txt')