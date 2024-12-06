#Verifica idade do cliente para curso de python idade minima
print('bem-vindo ao Senac')
print('Para fazer curso de python é necessário verificamos sua idade:')
idade = int(input())

if (idade<=15):
    print('Você não pode iniciar curso por conta da idade.')
else:
    print('Você pode iniciar curso Python!')