#gerar um numero secreto, tente acertar
import random
#Nivel dificuldade
nivel = int(input("Qual nível de dificuldade você deseja:\n1 - Facil\n2 - Medio\n3 - Dificil\nEscolha: "))
if(nivel == 1):
 dif = 200
elif(nivel == 2):
 dif = 500
else:
 dif = 900

#Tentativas
qcontador = int(input("Qual nível de dificuldade você deseja:\n1 - Facil = 10 tentativas\n2 - Medio = 7 tentativas\n3 - Dificil = 5 tentativas\nEscolha: "))
if(qcontador == 1):
 contador = 10
elif(qcontador == 2):
 contador = 7
else:
 contador = 5

#Gerador do número
secreto = random.randint (1, dif)
print(secreto)

print("Sistema gerou um numero secreto, tente acertar")

while (contador > 0):
    resposta = int(input("Qual número você acha que é: "))
    if(resposta > secreto):
        print (f"\nMenor, faltando {contador}")
        contador -= 1
    elif(resposta < secreto):
        print (f"\nMaior, faltando {contador}")
        contador -= 1
    else:
        print(f"\nVocê conseguiu!!\n")
        contador -= 10

print(f"seu numero era {secreto}.")

