
lista_amostras = [(62,173),(90,186),(76,212),(54,156),(69,176),(112,163),(98,159)]

def IMC(x):
    imc = round(x[0] / ((x[1]/100)**2),2)
    return imc
    
imc_list = list(filter(lambda x: x> 25,map(IMC,lista_amostras)))
print(imc_list)
