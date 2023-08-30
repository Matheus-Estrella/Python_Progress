import random

n_passageiros = lambda: random.randint(40, 150)
tot_passageiros = lambda v1,v2: list(map(lambda x,y: x+y, v1,v2))
ordenate = lambda lst: sorted(lst, reverse = True)
classify = lambda lst: [1 if (x <= 100 and x > 0) else 2 if (x <= 200 and x > 100) else 3 if (x > 200) else 0 for x in lst]

empresas = ['Gol','TAM','TAP']

voo1 = [n_passageiros() for x in range(len(empresas))]
voo2 = [n_passageiros() for x in range(len(empresas))]
total_voos = ordenate(tot_passageiros(voo1,voo2))
total_voos = list(zip(empresas,total_voos,classify(total_voos)))


print(total_voos)



