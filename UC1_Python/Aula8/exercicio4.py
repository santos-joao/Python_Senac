#Informe 4 numeros 

impar = 0
par = 0
for n in range (4):
    numero = int(input("Insira um numero: "))
    if(numero%2 == 0):
        par += numero
    else:
        impar += numero

print(f"Soma dos par: {par}\n Soma dos impares: {impar}")