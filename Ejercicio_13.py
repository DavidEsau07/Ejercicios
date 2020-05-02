def carac():
    
    x = str(input("\nIngrese una oración: "))
    #Elimina el primer caracter de la cadena
    print(x[1::])

    a = int(input("\nSeleccione 1 para volver a intentar, cualquier otro número para cerrar: "))
    if a == 1:
        return carac()
    else:
        print("\nGracias!")

print("\t\t Cadena sin el primer caracter")
carac()
