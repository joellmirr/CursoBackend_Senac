import os
os.system('clear')

print("Lista Alunos:")
listaAlunos = []
i = 0
while i != "-1":
  i = input("Informe Nome do Aluno:")
  if i == "-1":
    break
  listaAlunos.append(i)
print("Alunos: ",listaAlunos)

listaAlunos.pop(0)
listaAlunos.pop(3)
listaAlunos.pop(7)
listaAlunos.pop(8)
print("Alunos: ",listaAlunos)

x = listaAlunos.index('shalin')
print(x)

listaAlunos.sort()
print(listaAlunos)

notas = ()
listaNotas = []
i = 0
while i != "-1":
  i = input("Informe Nota do Aluno:")
  if i == "-1":
    break
  listaNotas.append(i)

notas = tuple(listaNotas)
print("Notas  dos Alunos: ",notas)

boletin = dict(zip(listaAlunos,notas))
print("Boletin: ",boletin)




