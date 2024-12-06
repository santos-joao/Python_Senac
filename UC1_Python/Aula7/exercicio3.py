#Programa que receba um numero e diga se é primo ou não

numero = int(input("insira um numero: "))
primo = True
for i in range (2, numero):
    if(numero%i == 0):
        primo = False
    
if ( primo == False):
    print("Esse número não é primo")
else:
    print("Esse é número primo")


