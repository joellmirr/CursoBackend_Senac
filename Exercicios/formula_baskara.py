print("Formula de Bhaskara:")

a = float(input("Digite Valor de A: "))
b = float(input("Digite Valor de B: "))
c = float(input("Digite Valor de C: "))

delta = (b**2) - ( 4*a*c)
print("Valor de Delta:", delta)

x1 = (-1*b - (delta ** (1/2))) / 2*a
x2 = (-1*b + (delta ** (1/2))) / 2*a

print("Valor X1:", round( x1, 2))
print("Valor X2:", round( x2, 2))
