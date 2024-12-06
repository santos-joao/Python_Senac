
''''
While -> Enquanto
 Equanto uma condição for verdadeira, o código "dentro" dele irá executar. Podemos chamar isso de loop!
 
 CUIDADO COM LOOPS INFINITOS!

'''

soma = 0
contador = 0

#solicita ao usuário que insira 5 números
while contador < 5:
    numero = float(input("Insira um número: "))
    soma += numero
    contador = 0

#exibe a soma total 
print(" A soma total é:", soma)