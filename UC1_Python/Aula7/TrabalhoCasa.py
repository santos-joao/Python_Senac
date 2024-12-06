# como saber qual cor vc deve jogar sua reciclagem  

print("-----Bem-vida!------\nEsse programa de reciclagem para ajudar planeta!!")
x = 0 
Papel = "lixeira azul."
Plastico = "lixeira vermelha."
Vidro =  "lixeira verde."
Metal = "lixeira amarela."
Organico = "lixeira marrom."
rnr = "lixeira cinza."
Q_Papel = 0
Q_Plastico = 0
Q_Vidro =  0
Q_Metal = 0
Q_Organico = 0
Q_rnr = 0  

while (x < 1):
 reciclagem = int(input("\nQual matérial você dceseja reciclar:\n1- Papel\n2- Plástico\n3- vidro\n4- Metal\n5- Orgânico\n6- Resíduos não recicláveis\nQuais das opções: "))
 #PAPEL
 if (reciclagem == 1):
      Q_Papel+= float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
      print(f"\nVocê deve jogar na {Papel}\n")
      novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
      if (novo == "s"):
         x = 0
      else:
         x += 1
 #PLASTICO      
 elif ( reciclagem == 2):
       Q_Plastico += float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
       print(f"\nVocê deve jogar na {Plastico}\n")
       novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
       if (novo == "s"):
         x = 0
       else:
         x += 1
  #VIDRO       
 elif ( reciclagem == 3):
       Q_Vidro += float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
       print(f"\nVocê deve jogar na {Vidro}\n")
       novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
       if (novo == "s"):
         x = 0
       else:
         x += 1
   #METAL      
 elif ( reciclagem == 4):
       Q_Metal += float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
       print(f"\nVocê deve jogar na {Metal}\n")
       novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
       if (novo == "s"):
         x = 0
       else:
         x += 1
   #ORGANICO       
 elif ( reciclagem == 5):
       Q_Organico += float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
       print(f"\nVocê deve jogar na {Organico}\n")
       novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
       if (novo == "s"):
         x = 0
       else:
         x += 1
   #Resíduos não recicláveis      
 elif ( reciclagem == 6):
       Q_rnr += float(input(f"\nQual quantidade você vai jogar fora(somente numero): "))
       print(f"\nVocê deve jogar na {rnr}\n")
       novo = input("\nVocê desejar continuar reciclando outro produtos? (S/N)\n").lower()
       if (novo == "s"):
         x = 0
       else:
         x += 1

 else:
    print("Erro tente novamente e não contabilizar na contagem de nenhuma lixeira.")       
    x = 0

somatotal = Q_Metal + Q_Organico + Q_Papel + Q_Plastico + Q_rnr + Q_Vidro
print(f"\n\n----------Obrigado por contribuir com a reciclagem!\nVocê reciclicou:\nPapel = {Q_Papel}\nPlástico = {Q_Plastico}\nVidro = {Q_Vidro}\nMetal = {Q_Metal}\nOrgânico = {Q_Organico}\nResíduos não recicláveis = {Q_rnr}\n No total foram {somatotal} de produtos recliclados!")
