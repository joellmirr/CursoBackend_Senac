import os 
os.system("cls")

print("1.Mostrar Numeros Impares ate 100:")
for i in range(1,100,2):
    print(i)

print("\n2.Mostrar Numeros Pares ate 100:")
for i in range(2,101,2):
    print(i)

print("\n3.Mostrar Numeros Multiplos de 10 entre 1 e 100:")
for i in range(1,101):
    if (i % 10 == 0):
        print(i)

print("\n4.Mostrar Numeros Multiplos tanto 2 quanto 3  entre 1 e 100:")
for i in range(0,101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

print("\n\n5.Exercicio Decresente:")

print("1.1.Mostrar Numeros Impares entre 100 e 1:")
for i in range(100,1,-2):
    print(i)

print("\n2.2.Mostrar Numeros Pares entre 100 e 1:")
for i in range(99,0,-2):
    print(i)

print("\n3.3.Mostrar Numeros Multiplos de 10 entre 100 e :")
for i in range(100,1,-10):
    if (i % 10 == 0):
        print(i)

print("\n4.4.Mostrar Numeros Multiplos tanto 2 quanto 3  entre 100 e 1:")
for i in range(101,1,-1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
