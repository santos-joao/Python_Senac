# Faça um programa que se o usuário inserir 1 , ele escolhe a classe bábaeo , se ele inserir 2 , ele escolhe a classe mago , se ele inserir 3 , ele escolhe a classe arqueiro.

classe = int(input('Eschola 1 para Bárbaro\n Escolha 2 para Mago\n Escolha 3 para Arqueiro'))
if(classe==1):
    Escolha = " Bárbaro" 
elif(classe==2):
    Escolha = "Mago"
else:
    Escolha = "Arqueiro"

Arma = int(input("\nEscolha 1 para arma longa\nEscolha 2 para arma curta:\n"))
if(Arma == 1):
    Selecao = "Longo Alcance"
else:
    Selecao = "Curto Alcance"
    
print(f"Você escolheu:\nClasse:{Escolha}\nArma:{Selecao}")