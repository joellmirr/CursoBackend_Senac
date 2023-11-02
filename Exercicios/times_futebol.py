import os
os.system('clear')

print("times Futebol")
time1=int(input("Digite Gols Goias:"))
time2=int(input("Digite Gols Vila:"))

if time1>time2:
    print("Vitoria do Goias")
elif time1==time2:
      print("Empate Goias x Vila2")   
else:
     print("Vitoria do Vila")
   