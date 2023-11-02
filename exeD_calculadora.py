import os
os.system('cls')

print("CALCULADORA")
i = 1
while i != 0:
    print("\nOperação Matematica:")
    numerador = float(input("Digite primeiro numero: "))
    denominador = float(input("Digite segundo numero: "))
    operacao = int(input("Digite Operação Matematica:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Sair do Programa:\n->"))
    match operacao:
        case 1:
            resultado = numerador + denominador
            print("Resultado:",resultado)
        case 2:
            resultado = numerador - denominador
            print("Resultado:",resultado)
        case 3:
            resultado = numerador * denominador
            print("Resultado:",resultado)
        case 4:
            if denominador!= 0:
                resultado = numerador / denominador
                print("Resultado:",resultado)
            else:
                print("Denominador Invalido!\nTente Novamente!")
        case 0:
            break
        case _:
            print("Opção Invalida")

