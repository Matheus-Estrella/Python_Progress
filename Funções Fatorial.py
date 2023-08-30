#Comparação de fatoriais por loop for e reduce

from functools import reduce 

def fatorial_for():
    
    n = int(input ("Para n!, digite o valor de n: "))
    fatorial = 1
    
    if n == 0:
            print(f'O fatorial de 0! é 1')
    else: 
        for i in range(1,n+1):
            fatorial *= i
            if i == n:
                print(f'O fatorial de {i}! é {fatorial}')
            
def fatorial_reduce():
        
    n = int(input ("Para n!, digite o valor de n: "))
    numeros = list(range(1,n+1)) if n!= 0 else [1]
    fatorial = reduce(lambda x,y: x*y if n != 0 else 1,numeros)
    print(f'O fatorial de {n}! é {fatorial}')
            
'''
fatorial_for()
fatorial_reduce()
'''