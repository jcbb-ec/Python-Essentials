def EsPrimo(n):
    for i in range(2,n):
        residuo=n%i
        if  residuo== 0:
            return False    
    return True
        

for i in range(1,20):
    if EsPrimo(i+1):
        print(i+1,end=" ")  