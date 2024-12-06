#Calcule o IMC(IMC = peso/altura x Altura) do cliente
print("Vamos calcular seu IMC do corpo")
print(" Poderia informar sua altura em metro:")
Altura = float(input())
print("Agora coloque seu peso em quilos:")
Peso = float(input())
print("Obrigado so um momento que estavamos calculando")
IMC = Peso/(Altura*Altura)
print(f"Seu IMC é {IMC}")