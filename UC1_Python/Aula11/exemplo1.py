
# funcoes.py

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao programa."

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)
   
 # main.py

from funcoes import calcular_area_retangulo, calcular_fatorial, saudacao
n = input("qual seu nome:")
mensagem = saudacao(n)
print(mensagem)

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = calcular_area_retangulo(base, altura)
print(f"A área do retângulo é: {area}")

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {fatorial}")