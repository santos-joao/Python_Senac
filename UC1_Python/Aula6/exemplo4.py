x = True
soma = 0
while (x==True):
    numero = float(input("Digite um numero:"))
    continuar = input("Continuar ou parar?").lower()
    if (continuar == "parar"):
        soma += numero
        x=False
        print(f"a soma deu {soma}")
    else:
        soma += numero

