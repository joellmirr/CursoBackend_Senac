import os
os.system('cls')

print("SEQUENCIA FIBANOCCI:")
primeiro = 1 
penultimo = 0
ultimo = 0
while penultimo <= 500:
    penultimo += primeiro 
    ultimo += penultimo
    primeiro = ultimo
    if ultimo >= 500:
        break
    print(penultimo,"\n",ultimo)
