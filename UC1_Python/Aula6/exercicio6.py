#peça dois numero e faça algumas das operações 1- soma 2- subtrai 3- Mult 4- Dividir

numero_1 = int(input("insira primmeiro numero: "))
numero_2 = int(input("insira segundo numero: "))

escolha = int(input(f"Você escolheu os numeros {numero_1} e {numero_2}, agora escolha uma das opções matematicas:\n1- Somar\n2- Subtrair\n3- Multiplicar\n4 - Dividir\nqual das operações: "))

if(escolha == 1):
     soma = numero_1 + numero_2
     print(f"{numero_1} + {numero_2} = {soma}")
elif(escolha == 2):
     subtrair = numero_1 - numero_2
     print(f"{numero_1} - {numero_2} = {subtrair}")
elif(escolha == 3):
     mult = numero_1 * numero_2
     print(f"{numero_1} x {numero_2} = {mult}")
elif(escolha == 4):
     dividir = numero_1 / numero_2
     print(f"{numero_1} + {numero_2} = {dividir}")
else:
     print("opção invalida, tente novamente")