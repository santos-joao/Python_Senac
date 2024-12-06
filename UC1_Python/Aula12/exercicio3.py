'''
O aventureiro e o assaltante atacam simultaneamente, causando dano um ao outro com o valor de "Ataque".
A batalha continua até que a "Vida" de um dos personagens chegue a zero ou abaixo.
Após cada rodada de ataque, o status de cada personagem (seus valores de "Vida" e "Ataque") deve ser exibido.
Haverá um intervalo de 4 segundos entre as rodadas de ataque para simular a pausa entre os golpes.
Ao final da batalha, o loop deve parar e os valores finais de "Vida" de ambos os personagens devem ser mostrados.

Escreva o código para simular essa batalha e exiba o status de ambos os personagens a cada rodada de ataque.

Faça um variável sorte, onde ela multiplica o ataque por até 20 ambos os personagens. 

'''
import time, random
Roude = 1
aventureiro = [
    ["Vida", "Ataque"],
    [1000, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [600, 20]
]

print("Aventureiro")
for linha in aventureiro:
     print(linha)
print(10 * "-")
print("Assaltante")   
for linha in assaltante:
     print(linha)

print("\nComeçou Batalha!!")
while(aventureiro[1][0] > 0 and assaltante[1][0] > 0):
     print(f"\nRoude {Roude}")
     Roude += 1
     #bonus
     bonus_aventureiro = random.randint (1, 20)
     bonus_assaltante = random.randint (1, 20)
     #ataque
     aventureiro[1][0] -= assaltante[1][1] * bonus_aventureiro
     assaltante[1][0]  -= aventureiro[1][1] * bonus_assaltante
     

     print(10 * "-")
     print("Aventureiro")
     for linha in aventureiro:
         print(linha)
     print(f"Ataque: {aventureiro[1][1] * bonus_aventureiro}")
     print(10 * "-")
     print("Assaltante")   
     for linha in assaltante:
         print(linha)
     print(f"Ataque: {assaltante[1][1] * bonus_assaltante}")
     time.sleep(4)
 