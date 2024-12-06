#programa que simule o armário de uma escola, possivel colocar nome do aluno a gaveta do armário tem dimensão 5x5
x = 0
responsavel = input("Qual seu nome ? ")
#os armarios
armario = [
    ["", "","","",""],
    ["", "","","",""],
    ["", "","","",""],
    ["", "","","",""],
    ["", "","","",""]
]


armario_vip = [
    ["", "",""],
    ["", "",""],
    ["", "",""]
]
#Escolha
escolha = int(input("Qual armário você gostário de alugar por 6 mês:\n 1 - Armário (5x5) normal custa R$ 30,00 ao mês\n 2- Armário VIP (3x3),fica do lado das salas, custa R$ 50,00 ao mês\n 3 - nada, não quero mais\nQual sua escolha?  "))
#armario simples
if(escolha == 1):
 while x  == 0:
    for i in armario:   
      print(i)
    arm = input("você gostária de colocar algo no seu armário ?").lower()
    if (arm == "sim" or arm == "s"):
        objeto = input("qual objeto ? ")
        linha = int(input("Em qual parte (0 x 4)?  "))
        coluna = int(input("Qual coluna gostário de colocar (0 x 4)? "))
        armario[linha] [coluna] = objeto
    else:
     print("Até proxima")
     x += 2
 print(f"O resposavél é {responsavel}")
 for i in armario:   
  print(i)
#Armario_vip
elif (escolha == 2):
 while x  == 0:
   for i in armario_vip:   
     print(i)
   arm = input("você gostária de colocar algo no seu armário ?").lower()
   if (arm == "sim" or arm == "s"):
        objeto = input("qual objeto? ")
        linha = int(input("Em qual parte (0 x 2)? "))
        coluna = int(input("Qual coluna gostário de colocar (0 x 2)? "))
        armario_vip[linha] [coluna] = objeto
   else:
     print("Até proxima")
     x += 2
   print(f"O resposavél é {responsavel}")
   for i in armario_vip:   
    print(i)
#Nada de armário
else:
  print("Volte mais tarde! Tenha boa aula")