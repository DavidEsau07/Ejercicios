def elimi():
    x = str(input("\nIngrese una palabra: "))
    print(x[1:-1])
    a = int(input("\n Ingrese 1 si quiere volver, cualquier otro número para salir: "))
    if a == 1:
            return elimi()
    else:
        print("\n\t¡Gracias!")

print("\t\t Cadenas sin el primer y último carácter")
elimi()
