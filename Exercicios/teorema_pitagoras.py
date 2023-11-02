print("Teorema de Pitagoras:")

co = float(input("Digite Valor Lado Cateno Oposto: "))
ca = float(input("Digite Valor Lado Cateno Adjacente: "))

h = (co**2 + ca**2) ** (1/2)
print("Valor Hipotenusa: ", h)

sen = co / h
cos = ca / h
tg = co / ca
print("Valor Seno: ", sen)
print("Valor Coseno: ", cos)
print("Valor Tangente: ", tg)