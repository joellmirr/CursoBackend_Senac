import os
os.system('clear')

#Ter no mínimo 65 anos de idade.
#Ter trabalhado no mínimo 30 anos.•
#Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos

print("Calculo Verificação Aposentadoria")
nome=input("Digite Nome do Trabalhador:")
idade=int(input("Digite Ano Nascimento:"))
tempo=int(input("Digite Ano Inicio Primeiro Trabalho:"))

idade=2023-idade
tempo=2023-tempo

if idade>=65 and tempo>=30 or idade>=60 and tempo>=25:
    print("Tabalhador:",nome,"\nIdade:",idade,"anos","\nTempo Trabalho:",tempo,"anos")
    print("Pode Requerer Aposentadoria")
else:
     print("Tabalhador:",nome,"\nIdade:",idade,"anos","\nTempo Trabalho:",tempo,"anos")
     print("Nao Pode Requerer Aposentadoria")
