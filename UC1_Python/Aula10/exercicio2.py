import random
#numeros
n1 = random.uniform (20, 50)
n2 = random.uniform (20, 50)
n3 = random.uniform (20, 50)
n4 = random.uniform (20, 50)
print(n1, n2, n3, n4)
loop = 1
while (loop == 1):
    if n2 > n1:
       n1,n2 = n2,n1
    if n3 > n2:
        n2,n3 = n3,n2
    if n4 > n3:
        n3,n4 = n4,n3
    if n4 < n3 and n3 < n2 and n2 < n1:
       print(f"ordem {n1}, {n2}, {n3}, {n4}")
       loop += 1
