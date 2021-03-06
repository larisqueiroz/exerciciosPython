"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além 
dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem 
sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
O formato da saída foi dado pela empresa, e é o seguinte:   

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

enquete = []
colocacao = []
SOs = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
percentual = []
total = []
while True:
    opcao = int(input(f'Qual o melhor Sistema Operacional para uso em servidores?\n1- Windows Server\
    \n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n0- Encerrar\nOpção:'))
    
    if opcao != 0:
        enquete.append(opcao)
    
    if opcao == 0:
        break

colocacao.extend([enquete.count(1), enquete.count(2), enquete.count(3), enquete.count(4), enquete.count(5), enquete.count(6)])

for item in colocacao:
    percentual.append(item/sum(colocacao)*100)
    
maior = max(colocacao)
for ind, valor in enumerate(colocacao):
    if valor == maior:
        ind_maioria_votos = ind

print('\nSistema Operacional\tVotos\t%')
print('---------------------\t-----\t---')
for i in range(6):
    if i == 0:
        print(f'{SOs[i]}\t\t{colocacao[i]}\t{int(percentual[i])}%')
    else:
        print(f'{SOs[i]}\t\t\t{colocacao[i]}\t{int(percentual[i])}%')
    
print('---------------------\t-----\n')
print(f'Total\t\t\t{sum(colocacao)}\n')
print(f'O Sistema Operacional mais votado foi o {SOs[ind_maioria_votos]}, com {colocacao[ind_maioria_votos]} \
votos, correspondendo a {int(percentual[ind_maioria_votos])}% dos votos.')
