#Faça um programa que imprima os 10 primeiros números da sequência de fibonacci
fibo_1 = 1
fibo = 0

for f in range (5):
    fibo_1 = fibo_1 + fibo
    print(fibo_1)
    fibo += fibo_1
    print(fibo)