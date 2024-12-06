# como saber qual cor vc deve jogar sua reciclagem  

print("-----Bem-vida!------\nEsse programa de reciclagem para ajudar planeta!!") 
ncard = int(input("Qual quantidade de cartas no jogo? "))
ponto = 0
nponto = int(ncard/2 + 1)
print(nponto)

while (ponto < nponto):
 reciclagem = int(input("\nQual matérial você tirou:\n1- Papel\n2- Plástico\n3- vidro\n4- Metal\n5- Orgânico\n6- Resíduos não recicláveis\nQuais das opções: "))
 #PAPEL
 if (reciclagem == 1):
     resposta = input("Qual cor da lixeira? ").lower()
     if (resposta == "azul"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
     else:
         print ("Erroooo!!!") 
 #PLASTICO      
 elif ( reciclagem == 2):
     resposta = input("Qual cor da lixeira? ").lower()
     if (resposta == "vermelha" or resposta == "vermelho"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
     else:
         print ("Erroooo!!!") 
  #VIDRO       
 elif ( reciclagem == 3):
     resposta = input("Qual cor da lixeira? ").lower()
     if (resposta == "verde"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
     else:
         print ("Erroooo!!!") 
   #METAL      
 elif ( reciclagem == 4):
      resposta = input("Qual cor da lixeira? ").lower()
      if (resposta == "amarelo"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
      else:
         print ("Erroooo!!!") 
   #ORGANICO       
 elif ( reciclagem == 5):
      resposta = input("Qual cor da lixeira? ").lower()
      if (resposta == "marrom"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
      else:
         print ("Erroooo!!!") 
   #Resíduos não recicláveis      
 elif ( reciclagem == 6):
      resposta = input("Qual cor da lixeira? ").lower()
      if (resposta == "cinza"):
         print("\nVocê ganhou um ponto!")
         ponto += 1 
      else:
         print ("Erroooo!!!") 

 else:
    print("Erro tente novamente e não contabilizar na contagem de nenhuma lixeira.")      

print (f"Você ganhou, compeltou {ponto} pontos")