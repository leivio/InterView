from decimal import *
#x =  [Decimal(10**1025),  Decimal(10**1025), Decimal(10**1025), Decimal(10**1025), Decimal(10**1025)]
#x =  [5, 4, 6, 3, 2] # 4 5 3 2 6

x =  [5, 20, 6, 3, 2, 8 , 7, 1] 
y = len(x) - 1 
for z in range(y):
    i = 0
    while i + 1 < len(x):
        if (x[i] > x[i + 1]):
           j = x[i + 1]
           q = x[i]
           x[i] = j
           x[i + 1] =  q    
        i += 1     
print(x)