'''
Created on Jan 13, 2023

@author: estudiante
'''

def generar_numero():
    from random import randint
    return randint(0,20)

def es_pass_segura(contraseña):
    tieneNumero=False
    segura=False
    numeros="0123456789"
    caracter="<!@"
    tieneCaracter=False
    espacio=" "
    noTieneEspacio=False
    for i in range(len(contraseña)):
        if contraseña[i] in numeros:
            tieneNumero=True
        elif contraseña[i] in caracter:
            tieneCaracter=True
        elif contraseña[i] not in espacio:
            noTieneEspacio=True
        
    if len(contraseña)>=8:
        if tieneNumero and tieneCaracter and noTieneEspacio:
            segura=True
    return segura
print(es_pass_segura('12345678'))
print(es_pass_segura('PxH1#n!8'))
assert(es_pass_segura('1235678')==False)
assert(es_pass_segura('PxH1#n!8')==True)
print("Todo correcto")


def generar_pass_segura():
    contraseña=""
    caracter="<!@"
    espacio=""
    while len(contraseña)<=8:
        contraseña+=str(generar_numero())+caracter+espacio
    return contraseña
        
print(generar_pass_segura())
    

    