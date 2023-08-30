def inserir_valores():
    num_list = []
    op = 1
    while op != 2:
        try:
            n = int(input('Digite um número inteiro: '))
            op = int(input('Deseja inserir outro número?\n1- Sim\n2- Não\n:'))
        except ValueError:
            print('\nInsira apenas números inteiros\n')
        num_list.append(n)
    return num_list

def is_prime(num_list):
    prime_list = []
    for i in num_list:
        prime = 0  
        for n in range(1, i + 1):
            if i % n == 0:
                prime += 1
        if prime == 2: 
            prime_list.append(i)
    yield prime_list

print(next(is_prime(inserir_valores())))
