import random;
import string as st;
from colorama import Fore, init;
init()
color = {
    'Green':Fore.GREEN,
    'Blue': Fore.BLUE,
    'Red': Fore.RED,
    'Reset': Fore.RESET,
}
lista_numeros = []
lista_caracteres = []
lista_senhas = []
letras = st.ascii_letters
lista_opsenhas = []
n = 1
caracteres_selecionados = [i for i in st.punctuation if i in '!@#&']
for l in st.ascii_letters:
    lista_caracteres.append(l)
    
    
    
for ce in caracteres_selecionados:
    lista_caracteres.append(ce)
    
    

for number in range(0,10):
    lista_numeros.append(number)
n_S = list(map(str, lista_numeros))

lista_caracteres.extend(n_S)



qc = int(input("Digite a quantidade de caracteres que voce deseja em sua senha: "))


qs = int(input('Digite a quantidade de senhas que voce deseja: '))

inicial = str(input("Digite seu nome para construirmos uma senha para voce ;) : "))


for y in range(qs):
    
    
    for i in range(qc):
        
        
        s = random.choice(lista_caracteres)
        
        
        lista_senhas.append(s)
    
     
    senha =''.join(lista_senhas)
    op_s = inicial+senha
    senha = op_s
    
    
    lista_opsenhas.append(senha)
    
    qs +=1
    lista_senhas = []
total_senhas = len(lista_opsenhas)

for senha in lista_opsenhas:
    print(f'senha numero {n}: {senha}')
    n+=1
    
    
while True:
    se = int(input('Digite o numero da senha desejada: '))
    if se > total_senhas or se <= 0:
        print("Este numero nao esta na senha")
    else:
        senhaescolhida = lista_opsenhas[se-1]
        break
        
        
        
print('-'*50)
print(f'Sua senha escolhida foi: {color["Green"]}{senhaescolhida}{color['Reset']}')