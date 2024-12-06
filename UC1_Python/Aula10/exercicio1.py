#Gerar programa que gerar 3 números aleatórios e uma tentativa de decobrir qual maior

import random
n1 = random.uniform (1, 15)
n2 = random.uniform (1, 15)
n3 = random.uniform (1, 15)
resp = int(input("qual é dos números aleatórios entre as 3 opções ficou com maior numero:\n1 -  Número 1\n2 - Número 2\n3 - numero 3\n: "))
#1 opção
if (resp == 1):
    if (n1 > n2 and n1 > n3):
        print("esse maior número, você acertou")
    else:
        print("você errou!!")
 #2 opção
elif (resp == 2):
    if (n2 > n1 and n2 > n3):
        print("esse maior número, você acertou")
    else:
        print("você errou!!")
 #3 opção
else:
    if (n3 > n2 and n3 > n2):
        print("esse maior número, você acertou")
    else:
        print("você errou!!")

print(f"Os número foram {n1}, {n2}, {n3}")