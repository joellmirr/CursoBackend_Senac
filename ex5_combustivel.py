import os
os.system('clear')

print("Promoçao Combustivel")
litros=float(input("Informe Qantidades de Litros:"))
combustivel=input("Digite A-Alcool ou G-Gasolina: ")

match combustivel.upper():
    case "A":
        quantidade=litros
        litros=round(litros*3.10,2)
        if quantidade<=20:           
            desconto=round(litros*0.03,2)
            valor=round(litros-desconto,2)
            print("Combustivel: Alcool.\nQuantidade:",quantidade,"Litros")
            print("Valor:R$",litros," - Valor Final com Desconto:R$",valor)
        else:
            desconto=round(litros*0.05,2)
            valor=round(litros-desconto,2)
            print("Combustivel: Alcool.\nQuantidade:",quantidade,"Litros")
            print("Valor:R$",litros," - Valor Final com Desconto:R$",valor)    
    case "G":
        quantidade=litros
        litros=round(litros*5.95)
        if quantidade<=20:           
            desconto=round(litros*0.04,2)
            valor=round(litros-desconto,2)
            print("Combustivel: Gasolina.\nQuantidade:",quantidade,"Litros")
            print("Valor:R$",litros," - Valor Final com Desconto:R$",valor)
        else:
            desconto=round(litros*0.06,2)
            valor=round(litros-desconto,2)
            print("Combustivel: Gasolina. Quantidade:",quantidade,"Litros")
            print("Valor:R$",litros," - Valor Final com Desconto:R$",valor)
    case _:
        print("Opção Invalida!")
