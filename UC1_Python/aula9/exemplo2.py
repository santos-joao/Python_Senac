'''
 Em funções passamos parâmetros (números, variáveis). Muitos vezes não temos acesso a lógica por trás. 
 Elas servem para facilitar o desenvolvimento e evitar códigos desencessários ou "a re-invenção da roda".
 Bibliotecas costumam ter várias funções.
 '''


import random

#gerar um número inteiro aleatório entre 1 e 100
numero_aleatorio = random.randint(1,100)
print(f"Número inteiro aleatório entre 1 e 100: {numero_aleatorio}")

#Solicitar para usuário selecionar um menor e mair número para "sorteio"
n_menor = int(input("Entre com numero menor deles: "))
n_maior = int(input("Entre com número maior deles: "))
n_aleatorio = random.randint(n_menor, n_maior)
print(f"Número inteiro aleatório entre {n_menor} e {n_maior}: {n_aleatorio}")
