'''
Created on Jan 13, 2023

@author: estudiante
'''
def generar_numero():
    from random import randint
    return randint(1,49)

print("Bienvenido al sorteo")

listaApuesta=[]
while len(listaApuesta)<=5:
    apuesta=int(input("Introduce los numero que deseas"))
    if apuesta>=1 and apuesta<=49:
        listaApuesta.append(apuesta)
    else:
        print("Los valores deben estar entre 1 y 49")
print(listaApuesta)

listaGanadora=[]
while len(listaGanadora)<=6:
    listaGanadora.append(generar_numero())

contador=0
for i in listaApuesta:
    for j in listaGanadora:
        if i==j:
            contador+=1
if contador==6:
    print("¡¡Enhorabuena!!Has triunfado!!")
else:
    print("No has acertado lo sentimos")
 

    