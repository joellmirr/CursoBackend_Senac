print("Calculo Peso Biologico")
altura = float(input("Digite Altura: "))
sexo = input("Digite m para masculino e f para feminino: ")

if(sexo == 'm'):
    print("Peso Biologico:",round(72.7 * altura -58))
elif(sexo == 'f'):
    print("Peso Biologico:",round(62.1 * altura - 44.7))
else:
    print("Digite Novamente.")




