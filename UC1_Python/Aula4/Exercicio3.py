#Calcule o IMC(IMC = peso/altura x Altura) do cliente
print("Vamos calcular seu IMC do corpo")
print(" Poderia informar sua altura em metro:")
Altura = float(input())
print("Agora coloque seu peso em quilos:")
Peso = float(input())
print("Obrigado so um momento que estavamos calculando")
IMC = Peso/(Altura**2)
print(f"Seu IMC é {IMC}")

if (IMC<18.5):
    print('Você está com magreza, Grau de obesidade 0')
elif (IMC>=18.5 and IMC<=24.9):
    print('Você está normal,Grau de obesidade 0')
elif (IMC>=25 and IMC<=29.9):
    print('Você esta com sobrepesoGrau de obesidade 1')
elif (IMC>=30 and IMC<=39.9):
    print('Você esta com obesidade, Grau de obesidade 2')
else:
    print('Você esta com obesidade grave,Grau de obesidade 3')