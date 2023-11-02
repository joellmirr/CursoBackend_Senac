import os
os.system('cls')

print("PESQUISA MERCADO PROFISSIONAIS TI:\n(para sair digite -1)")
valores = []
salario = 0
while salario >= -1:
    salario = float(input("Digite salario do profissional:R$"))
    if salario <= -1:
        break
    valores.append(salario)
print(valores)
media = sum(valores) / len(valores)
print("\nMedia Salarial:R$",media)
print("\nMenor Salario:R$", min(valores))
print("\nMaior Salario:R$",max(valores))

menoressalario = []
for i in valores:
    if i > media:
        menoressalario.append(i)
print("\nSalarios Maiores Media:",menoressalario)
maioressalario = []
for i in valores:
    if i < media:
        maioressalario.append(i)
print("\nSalario menores media:",maioressalario)
        