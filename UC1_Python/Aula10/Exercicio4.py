#Mude poder do Picachu
import time
contador = 5

poderes = ["Choque do trovão", "Calda de ferro", "Ataque rapido", "Esquiva"]
print(f"Lista de poderes do Pikachu {poderes}")
n_poder = (input("\nPikachu gostária de aprender Esfera Elétrica, gostário de ensinar? (s/n):  ")).lower()
#pergunta se pokemon que aprender
if (n_poder == "s" or n_poder == "sim"):
    troca = int(input("Por qual poder Pikachu:\n1 - Choque do trovão\n2 - Calda de ferro\n3 - Ataque rapido\n4 - Esquiva\n:  "))
    # Troca do primeiro poder
    if(troca == 1 ):
        print("\nPikachu esqueceu ataque Choque do trovão\n")
        while contador > 0:
         print(contador)
         time.sleep(1)
         contador -= 1
        print("\nPikachu aprendeu Esfera Elétrica")
        poderes[0] = "Esfera Elétrica"
    # Troca do segundo poder
    elif(troca == 2):
        print("\nPikachu esqueceu ataque Calda de ferro\n")
        while contador > 0:
         print(contador)
         time.sleep(1)
         contador -= 1
        print("\nPikachu aprendeu Esfera Elétrica")
        poderes[1] = "Esfera Elétrica"
    #Troca do segundo 
    elif(troca == 3):
        print("\nPikachu esqueceu ataque Ataque rapido\n")
        while contador > 0:
         print(contador)
         time.sleep(1)
         contador -= 1
        print("\nPikachu aprendeu Esfera Elétrica")
        poderes[2] = "Esfera Elétrica"
    else:
        print("\nPikachu esqueceu ataque Esquiva\n")
        while contador > 0:
         print(contador)
         time.sleep(1)
         contador -= 1
        print("\nPikachu aprendeu Esfera Elétrica")
        poderes[3] = "Esfera Elétrica"
else:
    print("\nPikachu não ira aprender Esfera Elétrica")

print(f"\nLista de poderes do Pikachu {poderes}")

        
