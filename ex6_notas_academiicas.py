import os
os.system('clear')

#Média > = 9.0 -> Conceito A
#Média > = 7.5 e Média < 9.0 -> Conceito B
#Média > = 6.5 e Média < 7.5 Conceito C
#Média < 6.5 -> Conceito D

print("Sistema Academico Notas Alunos")
aluno=input("Digite Nome do Aluno:")
nota1 = float(input("Digite Valor Nota 1: "))
nota2 = float(input("Digite Valor Nota 2: "))
nota3 = float(input("Digite Valor Nota 3: "))
media = round(float((nota1 + nota2 + nota3) / 3),2)

if media>=9.0:
    print("Aluno:",aluno,"Media:",media,"- Conceito A")
elif media>=7.5 and media<9.0:
    print("Aluno:",aluno,"Media:",media,"- Conceito B")
elif media>=6.5 and media<7.5:
    print("Aluno:",aluno,"Media:",media,"- Conceito C")
else:
    print("Aluno:",aluno,"Media:",media,"- Conceito D")
