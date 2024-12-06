#lavagem de carro
lavagem = int(input("   Seja bem-vindo!!    \nQual tipo de lavagem você gostária:\n1 -> Lavagem Completa = R$50,00\n2 -> Lavagem Básica = R$35,00\n"))
Completo= "Lavagem Completo"
Valor_Completo = 50
Basica = "Lavagem Basica"
Valor_Basica = 35
Pretinho = "Pretinho"
Valor_Pretinho = 5
if(lavagem == 1):
    print(f"Você escolheu {Completo}")
    Escolha = (input("Gostária de passar pretinho no pneu?\n")).lower()
    if(Escolha =="sim"):
        print(f"{Completo} + {Pretinho} fica no valor de R${Valor_Completo + Valor_Pretinho}")
    else:
        print(f"{Completo} fica no valor de R${Valor_Completo}")
elif(lavagem == 2):
    print(f"Você escolheu {Basica}")
    Escolha = (input("Gostária de passar pretinho no pneu?\n")).lower()
    if(Escolha =="sim"):
        print(f"{Basica} + {Pretinho} fica no valor de R${Valor_Basica + Valor_Pretinho}")
    else:
        print(f"{Basica} fica no valor de R${Valor_Basica}")
else:
    print("Codigo Invalido")

