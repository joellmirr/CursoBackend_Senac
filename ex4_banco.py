import os
os.system('clear')

print("Trasferencia Bancaria")
conta=int(input("Digite Numero da Conta:"))
saldo=float(input("Digite Valor do Saldo:R$"))
trasferencia=float(input("Digite Valor para Trasferencia:R$"))

if trasferencia<=saldo:   
    novaconta=trasferencia
    saldo-=trasferencia
    print("Conta:",conta,"Realizada Tranferencia:R$",trasferencia,".\nSaldo em Conta:R$",saldo)
else:
    print("Saldo Insuficiente!")
