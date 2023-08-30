''''
Faça um programa utilizando um arquivo chamado “NotasEscola.txt” para gerenciar as 
notas de alunos de uma classe. O main deve conter um menu com as seguintes opções:
a) Inserir alunos e notas 
b) Exibir os alunos e média final 
c) Alunos aprovados e reprovados 
d) Sair. Produza uma função para cada opção
'''
MediaAprov = 6
NotaMAX = 10
NotaMIN = 0

AskQnt = lambda: int(input("\nDigite o número de alunos para a operação: "))

def Menu(turma):
    valid = False
    while True:
        try:
            print("\n ----- MENU ----- ")
            print("a) Inserir alunos e notas\nb) Exibir alunos e média final\nc) Exibir aprovados e reprovados\nd) Sair")
            op = str(input("\nEscolha uma das opções acima: ")).lower()
            if op == 'a':
                nalunos = AskQnt()
                for i in range(nalunos):
                    turma = Inserir_Alunos_Notas(turma)
            elif op == 'b':
                Exibir_Alunos_Media(turma)
            elif op == 'c':
                Exibir_Aprovados_Reprovados(turma)
            elif op == 'd':
                break
            else:
                print("\nInsira uma opção válida")
        except ValueError:
            print("\nDigite uma opção válida")

        
def Inserir_Alunos_Notas(turma):
    aluno = {'Nome':'','N1':0,'N2':0,'Media':0,'Status':''}
    aluno['Nome'] = input("Digite o nome do aluno: ")
    
    for nota_nome in [('N1', 'primeira'), ('N2', 'segunda')]:
        while True:
            aluno[nota_nome[0]] = round(float(input(f"Digite a {nota_nome[1]} nota: ")), 2)
            if 0 <= aluno[nota_nome[0]] <= 10: 
                break 
            else:
                print(f"Nota fora do intervalo válido (0 a 10), tente novamente.")
    
    aluno['Media'] = (aluno['N1'] + aluno['N2']) / 2 
    aluno['Status'] = 'A' if aluno['Media'] >= MediaAprov else 'R'
    turma.append(aluno)
    with open('NotasEscola.txt','w') as arq:
        arq.write(str(turma))
    return turma

def Exibir_Alunos_Media(turma):
    for i in range(len(turma)):
        print(f"\nAluno: {turma[i]['Nome']}, Média: {turma[i]['Media']}")

def Exibir_Aprovados_Reprovados(turma):
    for i in range(len(turma)):
        print(f"\nAluno: {turma[i]['Nome']}, Situação: {turma[i]['Status']}")


#-------------------------------------------------------------------------------

turma = []
Menu(turma)
    
#-------------------------------------------------------------------------------
    