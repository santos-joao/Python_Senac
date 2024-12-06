#Quantas rodas tem um veiculo
print('Quantas rodas tem seu veiculo?')
Qrodas = int(input())
if (Qrodas==4):
    print('Isso é carro ou van')
elif (Qrodas==2):
    print('Isso é uma moto ou bicicleta')  
elif (Qrodas==6):
    print('Isso é um onibus')  
elif (Qrodas>=8 and Qrodas<=20):
    print('Isso é um caminhao') 
elif (Qrodas==1):
    print('Isso é um monociclo')     
else:
    print('Veiculo não encontrado')
