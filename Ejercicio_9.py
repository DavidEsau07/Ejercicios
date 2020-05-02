def may():
    
    lista = []

    for i in range (10):
        x=int(input("Ingrese número: "))
        lista.append(x)

    lista.sort(reverse = True)
    print("\n Los números ordenados de mayor a menor son: \n",lista)
    v = int(input("\nSeleccione 1 para volver a intentar, cualquier otro número para salir: "))
    if v == 1:
        return may()
    else:
        print("\n\t ¡Gracias!")

print("\t Mayor a menor")
may()
