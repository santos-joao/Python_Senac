'''
Apos a aventura da aula passada, o aventureira resolveu treinar mais seu combate;
faça uma simulação onde o aventureiro tem uma lista [100,20], onde 100 é vida dele e 20 é poder de ataque dele e a cada 7 segundos de treino, ele aumenta poder em 1, sendo limite maximo de 30 para seu poder de ataque
'''
import time
x = 0
tempo = 1
aventureiro = [100,20]

while x == 0:
  treino = input("Vamos treinar? ").lower()
  if(treino == "sim" or treino == "s"):
     if (aventureiro[1] < 30):
         print("Vamos La!!")
         while tempo < 8:
            print(tempo)
            time.sleep(1)
            tempo += 1
         aventureiro[1] += 1
         print(f"seu poder aumento para {aventureiro[1]}")
     else:
        print(f"Você chegou ao seu limite, seu poder atual é {aventureiro[1]}")
        x += 2
  else:
       print("Okay, agora vamos descansar!!")
       x += 0 


#Diferente
#Exercicio de treinamento do aventureiro
import time
aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
for linha in aventureiro:
    print(linha)
print("o treino começou!")
while  aventureiro[1][1] < 30:
    aventureiro[1][0] += 1
    print("o poder de ataque atual é", aventureiro[1][1])
    time.sleep(7)
print("Status final:")
for linha in aventureiro:
    print(linha)