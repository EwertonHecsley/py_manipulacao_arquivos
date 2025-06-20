import os
import shutil
from pathlib import Path

#Pega o caminho relativo da pasta onde o script está localizado.
ROOT_PATH = Path(__file__).parent

#Comando para criar um nvo diretório dentro do caminho especificado.
os.mkdir(ROOT_PATH / 'novo_diretorio')

#Comando para "escrever" ("W") criar um arquivo de um diretório para outro.
arquivo = open(ROOT_PATH / 'novo_diretorio'/'novo_arquivo.txt', 'w')
arquivo.close()

#Alterar nome do arquivo
os.rename(ROOT_PATH/'novo_diretorio'/'novo_arquivo.txt', ROOT_PATH/'novo_diretorio'/'arquivo_alterado.txt')