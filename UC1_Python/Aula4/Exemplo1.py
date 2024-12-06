'''
Se ->if
Caso contrario (Então) -> else
e -> and
'''
#Sou obrigadoa votar?
print('Ola, gostária de saber se você é obrigado votar esse ano, por favor informe sua idade:')
idade = int(input())
if (idade>=18 and idade<=65):
        print("sim vocês é obrigado a votar")
else:
    print("Não, você não é obrigado a votar")