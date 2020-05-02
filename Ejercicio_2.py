def invert():
    x=str(input("Ingrese un Nombre: "))
    print("\n",x[::-1])
    v = int(input("\n Seleccione 1 para volver a intentar, cualquier otro número para salir: "))
    if v == 1:
        return invert()
    else:
        print("\n\t ¡Gracias!")

print("\tNombres invertidos")
invert()
