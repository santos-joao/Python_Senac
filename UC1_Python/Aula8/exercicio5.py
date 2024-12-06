#Faça um programa que mostre os 20 primeiros multiplos de 5 que são pares
soma_total = 0
soma_par = 0
soma_imp = 0
for m in range(5, 101, 5):
    soma_total += m 
    if(m%2 == 0):
        print(m)
        soma_par += m
        
    else:
        soma_imp += m  
        
print(f"\nSoma dos impares é {soma_imp}\nSoma dos pares é {soma_par}\nSoma total da {soma_total}")