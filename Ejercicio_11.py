def flot():
    lista = []
    for i in range (3):
        x=float(input("Ingrese un número: "))
        lista.append(x)
        if x >= 1 and x <= 10:
            lista.sort(reverse = True)
        else:
            print("\n¡Tiene que ser entre '1.0' y '10.0'!")
            return flot()
    lista.sort(reverse = True)
    print(lista)
    a = lista[0]
    print("\nEl número más grande es:")
    if a >= 1 and a <2:
        print(a,"Uno")
    if a >= 2 and a <3:
        print(a,"Dos")
    if a >= 3 and a <4:
        print(a,"Tres")
    if a >= 4 and a <5:
        print(a,"Cuatro")
    if a >= 5 and a <6:
        print(a,"Cinco")
    if a >= 6 and a <7:
        print(a,"Seis")
    if a >= 7 and a <8:
        print(a,"Siete")
    if a >= 8 and a <9:
        print(a,"Ocho")
    if a >= 9 and a <10:
        print(a," Nueve")
    if a == 10:
        print(a,"Diez")

    v = int(input("\nSeleccione 1 para volver a intentar, cualquier otro número para salir: "))
    if v == 1:
        return flot()
    else:
        print("\n\t ¡Gracias!")
        
print("\t Número mayor (letra)")
print("\nElija 3 números flotante entre 1.0 y 10.0")
flot()


