'''

Input -> Comando para receber uma informação do usuário. 
input normalmente é utilizado após sinal de "=", onde atribuita um valor a uma variavel

'''
#Imprimir mensagem de boas-vidas personalizado
Nome =  input("qual seu nome?")
Sobrenome = input("Qual seu sobrenome?")
Meionome = input("Qual seu nome do meio?")
Ultimonome = input("Qual seu ultimo nome?")
#formas de imprimir na tela
#1
print(Nome)
print(Sobrenome)
print(Meionome)
print(Ultimonome)
#2
print(Nome,Sobrenome,Meionome,Ultimonome)
#3
print(Nome+" "+Sobrenome+" "+Meionome+" "+Ultimonome)