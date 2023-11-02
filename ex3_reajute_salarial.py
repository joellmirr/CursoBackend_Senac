import os
os.system('clear')

#Estagiário: 5% de aumento
#Nível Júnior: 7,5% de aumento
#Nível Pleno: 10% de aumento
#Nível Sênior: 12,5% de aumento

print("Reajuste Salarial")
nome=input("Digite Nome:")
salario=float(input("Digite Valor do Salario:R$"))

nivel=int(input("Digite Numero Nivel: 1.Nivel Senior  2.Nivel Pleno  3.Nivel Junior 4.Estagiario: "))
match nivel:
    case 1:
        nivel=0.125
        salario+=nivel*salario
        print("Funcionario",nome,"Nivel Senior - Reajuste Salario:R$",salario)
    case 2:
        nivel=0.1
        salario+=nivel*salario
        print("Funcionario",nome,"Nivel Pleno - Reajuste Salario:R$",salario)
        
    case 3:
        nivel=0.075
        salario+=nivel*salario
        print("Funcionario",nome,"Nivel Junior - Reajuste Salario:R$",salario)
    case 4:
        nivel=0.05
        salario+=nivel*salario
        print("Funcionario",nome,"Nivel Estagiario - Reajuste Salario:R$",salario)        
    case _:
        print("opção invalida!")

