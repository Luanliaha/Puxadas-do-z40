import subprocess
import os
import requests
from bs4 import BeautifulSoup
from faker import Faker
import random
import webbrowser

os.system('clear')

cor_vermelha = "\033[91m"
cor_azul_escuro = "\033[34m"
reset_cor = "\033[0m"

def main():
    print('  ──▒▒▒▒▒▒───▄████▄')
    print('  ─▒─▄▒─▄▒──███▄█▀')
    print('  ─▒▒▒▒▒▒▒─▐████──█─█')
    print('  ─▒▒▒▒▒▒▒──█████▄')
    print('  ─▒─▒─▒─▒───▀████▀')
    print(' ----------------Digite a opção desejada------------')    
    print(cor_vermelha + ' [1] - CNPJ' + reset_cor) 
    print(cor_vermelha + ' [2] - CEP' + reset_cor)
    print(cor_vermelha + ' [3] - CPF' + reset_cor) 
    print(cor_vermelha + ' [4] - SAIR' + reset_cor)
    escolha = input(cor_azul_escuro + "Digite o número da opção desejada:  " + reset_cor)
    
    if escolha == '1':
        subprocess.run(['python3', 'CNPJ.py'])
    elif escolha == '2':
        subprocess.run(['python3', 'CEP.py'])   
    elif escolha == '3':
        subprocess.run(['python3', 'script.py.py'])
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()

