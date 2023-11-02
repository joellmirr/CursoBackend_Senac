import os
os.system('clear')

print("Custo Carro")
custo=float(input("Digite Valor Custo Fabrica:R$"))
imposto=custo*0.45

categoria=int(input("Digite Numero Categoria do Veiculo: 1.Utilitario  2.SUV  3.Camionete: "))
match categoria:
    case 1:
        categoria=0.2
        categoria*=custo
        valorVeiculo=custo+imposto+categoria
        print("Veiculo Utilitario:")
        print("Custo Fabricação:R$",custo,"\nImpostos:R$",imposto,"\nMargem de Lucro:R$",categoria)
        print("Valor  Final Veiculo:R$",valorVeiculo)
    case 2:
        categoria=0.25
        categoria*=custo
        valorVeiculo=custo+imposto+categoria
        print("Veiculo Utilitario:")
        print("Custo Fabricação:R$",custo,"\nImpostos:R$",imposto,"\nMargem de Lucro:R$",categoria)
        print("Valor  Final Veiculo:R$",valorVeiculo)
        
    case 3:
        categoria=0.3
        categoria*=custo
        valorVeiculo=custo+imposto+categoria
        print("Veiculo Utilitario:")
        print("Custo Fabricação:R$",custo,"\nImpostos:R$",imposto,"\nMargem de Lucro:R$",categoria)
        print("Valor  Final Veiculo:R$",valorVeiculo)
       
    case _:
        print("opção invalida!")






