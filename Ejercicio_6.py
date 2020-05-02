def tex():
    a=str(input("\nIngrese texto a guardar: "))
    #a = Guardar
    #w = Limpiar
    file = open("Ejercicio_6.txt","w")
    file.write(a)
    file.close()
     #Regresar o Salir
    v = int(input("\nSeleccione 1 para volver a intentar, cualquier otro número para salir: "))
    if v == 1:
        return archi()
    else:
        print("\n\t ¡Gracias!")

print("\t\t Texto nuevo")
tex()
