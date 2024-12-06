import random

#gerando 4 números aleatórios e armazenando e uma lista
numeros = [random.randint(20, 50) for i in range (10)]

#exibindo os números gerados
print(f"Números gerados: {numeros}")

#Ordenando os números com função sort
numeros.sort()
numeros.reverse()

print (F"Números ordenados: {numeros}")