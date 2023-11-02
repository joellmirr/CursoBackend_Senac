import os
os.system('clear')

print("Promoção Chocolates")

barra=int(input("Digite Quantidades de Barras:"))
valor=0

valor+=barra//3*10
valor+=barra%3*4
print("Valor Barra Chocolate:",valor)

#quantidade=valor%3
#if (quantidade%3)!=0:
#   print("Valor Barras:R$",valor*4)
#elif (quantidade%3)==0:
#   valor/=3
#    print("Valor Barras:R$",valor*10)



   