'''
1) Faça uma função que receba um número inteiro maior que zero e retorne a
soma de todos os algarismos.
Caso o valor seja negativo retorne Numero invalido
'''

def digitsum(num):
    divisor = 1
    digit_num = 0
    while True:
        if (num // divisor) == 0:
            break
        else:
            digit_num += 1
            divisor *= 10
    soma = 0
    for i in range(digit_num):
        soma += ((num // (10 ** i))%10)
    return soma
    
print(digitsum(12345))