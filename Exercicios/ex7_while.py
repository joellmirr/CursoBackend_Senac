import os 
os.system("cls")

print("1.Mostrar Numeros Impares ate 100:")
i=1
while i<=100:
    if i % 2 != 0:
        print(i)
    i+=1

print("\n2.Mostrar Numeros Pares ate 100:")
i=1
while i<=100:
    if i % 2 == 0:
        print(i)
    i+=1

print("\n3.Mostrar Numeros Multiplos de 10 entre 1 e 100:")
i=1
while i<=100:
    if (i % 10 == 0):
        print(i)
    i+=1
print("\n4.Mostrar Numeros Multiplos tanto 2 quanto 3  entre 1 e 100:")
i=1
while i<=100:
    if i % 2 == 0:
        print("Multiplos de 2:",i)
    elif i % 3 == 0:
        print("Multiplos de 3:",i)
    i+=1

print("\n\n5.Exercicio Decresente:")

print("1.1.Mostrar Numeros Impares entre 100 e 1:")
i=100
while i<=100:
    if i % 2 != 0:        
        print(i)
    elif i==0:
        break
    i-=1

print("\n2.2.Mostrar Numeros Pares entre 100 e 1:")
i=100
while i<=100:
    if i % 2 == 0:        
        print(i)
    elif i==1:
        break
    i-=1
print("\n3.3.Mostrar Numeros Multiplos de 10 entre 100 e :")
i=100
while i<=100:
    if (i % 10 == 0):
        print(i)
    elif i==1:
        break
    i-=1
print("\n4.4.Mostrar Numeros Multiplos tanto 2 quanto 3  entre 100 e 1:")
i=100
while i<=100:
    if i % 2 == 0:
        print("Multiplos de 2:",i)
    elif i % 3 == 0:
        print("Multiplos de 3:",i)
    elif i==1:
        break
    i-=1
    
    
   

