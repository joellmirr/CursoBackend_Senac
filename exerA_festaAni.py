import os
os.system('cls')

print("Retire ate 200 doces:")
doce = 200
convidado=int(input("Digite quantidade retirada: "))
if convidado == doce:
    print("Acabou doces")
else:
    while convidado <= doce:
        doce-=convidado
        print("Doces Restantes:",doce)
        convidado=int(input("Digite quantidade retirada: "))
        if convidado > doce:
            print("quantidade doce insuficiente")
            print("entregue restantes docer disponiveis:",doce)
            break
        elif doce == convidado:
            print("Acabou doces!")
            break
    
  
