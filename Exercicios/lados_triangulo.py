import os
os.system('clear')

print("Tipo de Triangulo")
a=float(input("Diga Valor Lado A:"))
b=float(input("Diga Valor Lado B:"))
c=float(input("Diga Valor Lado C:"))

if a==b==c:
    print("Triangulo Equilatero")
elif a==b or a==c or b==c:
    print("Triangulo Isoceles")
else:
    print("Triangulo Escaleno")