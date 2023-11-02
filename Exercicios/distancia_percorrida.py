print("Calculo Distancia Percorrida:")

saida = float(input("Digite Horario de Partida: ")) 
chegada = float(input("Digite Horario de Chegada: "))
tempo = chegada - saida
print("Horario de Viagem: ", tempo)

distancia = float(input("Digite Distancia: "))
velocidade = distancia / tempo
print("Velocidade: ", velocidade,"Km/h")

