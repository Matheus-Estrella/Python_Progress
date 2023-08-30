'''
1 - Maria e Joao estão jogando bingo em família. Cada um possui uma cartela
e cada cartela possui 7 números entre 1 e 30, que serão sorteados por uma
função, utilizando choice(), contida em um módulo customizado, sendo
acessada apenas se o módulo for importado. Os números das cartelas devem
ser definidos utilizando comprehensions e choice() no programa principal. O
primeiro a ter seus 7 números chamados vence. Crie um sistema para
representar o jogo, como os numeros sorteados e a conferência das cartelas.
No final apresente o vencedor, os números da cartela do vencedor e os
números sorteados.
'''

from random import randint, shuffle, sample

#cartela = lambda: [randint(1, 30) for i in range(7)] --> Nâo gera os números diferentes, pode ocorrer erro de dupicidade
cartela = lambda: sample(range(1, 31), 7)

numeros = [num for num in range(1,31)]
shuffle(numeros)

player_name = lambda x: input(f'Digite o nome do {x}º jogador: ')
p1 = player_name(1)
p2 = player_name(2)

cartela_p1 = cartela()
winp1 = 0
winp2 = 0
cartela_p2 = cartela()

print(f'Cartela {p2}: {cartela_p2}\nCartela {p1}: {cartela_p1}\n')
print(f'Ordem sorteados: {numeros}')

for i in range(0,30):
    if winp2 != 7 and winp1 != 7:
        for x in (range(7)):
            if numeros[i] == cartela_p1[x] or numeros[i] == cartela_p2[x]:
                print(f'{i+1}º número sorteado: {numeros[i]}')
            if numeros[i] == cartela_p1[x]:
                winp1 += 1
                print(f'({p1} acertou: {cartela_p1[x]}, pontuacao: {winp1})')
            if numeros[i] == cartela_p2[x]:
                winp2 += 1
                print(f'({p2} acertou: {cartela_p2[x]}, pontuacao: {winp2})')
    
            