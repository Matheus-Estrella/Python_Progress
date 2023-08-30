import random

def avaliate():
    return random.randint(0, 100)

nomes = ['matheus', 'uriel','marina','daniele','felipe']

sport1 = [avaliate() for i in nomes]
sport2 = [avaliate() for i in nomes]
sport3 = [avaliate() for i in nomes]

total = [(sport1[i]+sport2[i]+sport3[i]) for i in range(len(nomes))]
print(list(zip(nomes, total)))


