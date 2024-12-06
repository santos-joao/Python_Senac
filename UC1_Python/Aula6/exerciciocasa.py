#Fazer calculo de soma  
Soma = float(input("-----Vamos fazer Calculo-----\nCalculo de hoje vai ser somas de numeros, poderia informar um numero:\n"))
Soma += float(input("Poderia inserir um segundo numero:\n"))
print(f"A soma desses dois numeros é: {Soma}\n")
Soma = Soma + float(input("Agora poderia inserir o terceiro numero:\n"))
print(f"A soma dos numeros é: {Soma}\n")
Soma += float(input("Poderia inserir o quarto numero:\n"))
Soma = Soma + float(input("Poderia também inserir o quinto numero:\n"))
print(f"A soma de todos os numeros é: {Soma}\n")