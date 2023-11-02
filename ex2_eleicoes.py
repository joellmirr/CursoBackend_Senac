import os
os.system('clear')

print("Eleiçoes Municipais")
agnaldo=int(input("Votos Agnaldo:"))
belmiro=int(input("Votos Belmiro:"))
carlito=int(input("Votos Carlito:"))
brancos=int(input("Votos Brancos e Nulos:"))

total=agnaldo+belmiro+carlito+brancos
agnaldo/=total
belmiro/=total
carlito/=total
brancos/=total

if agnaldo==belmiro and agnaldo==carlito and carlito==belmiro:
    print("Empate entre todos candidatos\nEleição será anulada e um novo pleito deverá ser convocado.")
elif brancos > 0.25:
    print("\nSegundo Turno")
    primeiroColocado=0
    if agnaldo>=belmiro and agnaldo>=carlito:
        primeiroColocado=agnaldo
        print("Primeiro Colocado: Agnaldo")
        if belmiro>=carlito:
            print("Segundo Colocado: Belmiro")
        else:
            print("Segundo Colocado: Carlito")
    elif belmiro>=agnaldo and belmiro>=carlito:
        primeiroColocado=belmiro
        print("Primeiro Colocado: Belmiro")
        if agnaldo>=carlito:
            print("Segundo Colocado: Agnaldo")
        else:
            print("Segundo Colocado: Carlito")
    elif carlito>=agnaldo and carlito>=belmiro:
        primeiroColocado=carlito
        print("Primeiro Colocado: Carlito")
        if agnaldo>=belmiro:
            print("Segundo Colocado: Agnaldo")
        else:
            print("Segundo Colocado: Belmiro")
elif agnaldo==belmiro or agnaldo==carlito or belmiro==carlito:
    print("\nEmpate-Segundo Turno")
    primeiroColocado=0
    if agnaldo>=belmiro and agnaldo>=carlito:
        primeiroColocado=agnaldo
        print("Primeiro Colocado: Agnaldo")
        if belmiro>=carlito:
            print("Segundo Colocado: Belmiro")
        else:
            print("Segundo Colocado: Carlito")
    elif belmiro>=agnaldo and belmiro>=carlito:
        primeiroColocado=belmiro
        print("Primeiro Colocado: Belmiro")
        if agnaldo>=carlito:
            print("Segundo Colocado: Agnaldo")
        else:
            print("Segundo Colocado: Carlito")
    elif carlito>=agnaldo and carlito>=belmiro:
        primeiroColocado=carlito
        print("Primeiro Colocado: Carlito")
        if agnaldo>=belmiro:
            print("Segundo Colocado: Agnaldo")
        else:
            print("Segundo Colocado: Belmiro")
else:
    if agnaldo>belmiro and agnaldo>carlito:
        print("Vitoria do Candidato Agnaldo")
    elif belmiro>agnaldo and belmiro>carlito:
        print("Vitoria do Candidato Belmiro")
    elif carlito>agnaldo and carlito>belmiro:
        print("Vitoria do Candidato Carlito")



