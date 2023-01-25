def comprobar_boleto(combinacion,lista):
    contador=0
    if len(combinacion)!=6:
        print("Debe haber 6 bolas")
    else:
        if len(lista)!=6:
            print("Debe haber 6 apuestas de numeros")
        else:
            for i in combinacion:
                for j in lista:
                    if i==j:
                        contador+=1
    return contador
    
print(comprobar_boleto([1,4,8,10,14,3],[1,2,3,4,10,14]))
assert(comprobar_boleto([1,4,8,10,14,3],[1,2,3,4,10,14])==5)




    
