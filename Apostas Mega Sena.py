from random import randint

ValoresApostas = { 6:5,7:35,8:140,9:420,10:1050,11:2310,12:4620,13:8580,14:15015,15:25025 }
            
def CustoApostas(Ncasas):
    global ValoresApostas
    for key, value in ValoresApostas.items():
        if Ncasas == key:
            return value


def LotoNumbers(NumCasas):
    return [randint(1, 60) for _ in range(NumCasas)]

def formatar_aposta(aposta, sorteio_num):
    return ', '.join(f'{num}' for i, num in enumerate(aposta, start=sorteio_num - 1))

def LotoRoll(NcasaPTRN):
    Jogos = []
    op = int(input("\nMENU\n1- Adicionar Apostas\n2- Sair\n: "))
    while op != 2:
        jogador = input("\nDigite o nome do apostador: ")
        if NcasaPTRN == 0:
            Ncasas = 6
        else:
            Ncasas = int(input("Digite o número de dezenas a serem sorteadas: "))
            while Ncasas < 6 or Ncasas > 15:
                print("Digite um valor entre 6 e 15")
                Ncasas = int(input("Digite o número de dezenas a serem sorteadas: "))
        Njogos = int(input("Digite o número de jogos a serem feitos: "))
        Apostas = []
        Custo = Njogos * CustoApostas(Ncasas)
        for i in range(Njogos):
            Apostas.append(LotoNumbers(Ncasas))
        Jogos.append((jogador, Apostas, Custo))
        op = int(input("\nMENU\n1- Adicionar Apostas\n2- Sair\n: "))
    return Jogos

with open('Apostas_Mega_Sena.txt', 'w') as arqv:
    apostas = LotoRoll(8)
    for jogador, jogador_apostas,custo in apostas:
        arqv.write(f'{jogador} apostou {custo},00 reais nos seguintes números:\n')
        for i, aposta in enumerate(jogador_apostas, start=1):
            arqv.write(f'   Jogo {i}: {formatar_aposta(aposta, i)}\n')
