'''
Created on Jan 13, 2023

@author: estudiante
'''
print("Bienvenido al Jacaixa")
menu='''
1.Abrir cuenta
2.Introducir nuevo valor de cambio
3.Comprar bitcoins
4.Vender bitcoins
5.Mostrar historico
6.Salir del programa
'''
opcion=1
banco=0
bancoB=0
lista=[]
MAXIMO=7
contador=0
cambio=16295.7
while opcion!=4:
    if opcion==1:
        saldo=float(input("Introduce el saldo de la cuenta corriente"))
        saldoB=float(input("Introduce el saldo de bitcoins"))
        if saldo<0:
            print("El saldo debe ser mayor que 0.Vuelva a intentarlo")
        else:
            banco+=saldo
        if saldoB<0:
            print("El saldo de bitcoins debe ser mayor que 0.Vuelva a intentarlo")
        else:
            bancoB+=saldoB
    elif opcion==2:
        valor=float(input("Introduce un valor a la lista"))
        if contador<=MAXIMO:
            lista.append(valor)
        else:
            lista[contador%MAXIMO]=valor
        contador+=1
    elif opcion==3:
        if banco<=0:
            print("No dispones de saldo suficiente")
        else:
            bitcoin=float(input("Introduce el bitcoin que deseas"))
            for i in range(len(lista)):
                if bitcoin==lista[i]:
                    compra=bitcoin*cambio
                    banco-=compra
                    bancoB+=bitcoin    
                else:
                    print("No se ha registrado ese valor de cambio")
    elif opcion==4:
        bitcoin=float(input("Introduce el bitcoin que deseas"))
        for i in range(len(lista)):
            if bitcoin==lista[i]:
                vende=bitcoin*cambio
                banco+=vende
                bancoB-=bitcoin
            else:
                print("No se ha registrado ese valor de cambio")
        
    elif opcion==5:
        print(lista)
    else:
        print(f"Saldo final : {banco} ")
        print(f"Saldo Final B: {bancoB}")
        
        
    print(menu)
    opcion=int(input("Introduce la opcion que deseas"))
    

        
    
        