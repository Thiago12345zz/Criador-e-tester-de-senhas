import creator
from creator import senhaescolhida
from creator import color
import string as st
from selenium import webdriver
import time


def website():
    while True:
        navegador = webdriver.Chrome()
        navegador.get("https://password.kaspersky.com/pt/")
        navegador.maximize_window()
        quit = print(str(input('Aperte enter para fechar o site: ')))
        if quit == '':
            navegador.quit()
            print('Finished!')
            break
    
def contagem_regressiva(x):
    while x > 0:
        print(f"Em {x}.")
        time.sleep(1)
        x -= 1
    website()

def login():
    dsenha = str(input("Digite sua senha escolhida:"))
    if dsenha == senhaescolhida:
        print(f'{color['Blue']}Acesso permitido{color['Reset']}')
        print("Iremos te direcionar para uma pagina web, para testar a potencia de sua senha!!!!!!!!!!!!!!!!!!!!!!!")
        contagem_regressiva(5)
        
    elif dsenha != senhaescolhida:
        print(f'{color['Red']}Acesso negado{color['Reset']}')
        
login()