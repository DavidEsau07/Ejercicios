import sys
print("\t Conversion de flotante a entero")
def red():
    x=float(input("Ingrese número flotante: "))
    print (round(x))
    a=float(input("\nPulse '1' para intentar de nuevo, cualquier otro número para salir: "))
    if a == 1:
        return red()
    else:
        print("\tGracias por usar mi programa!")

red()

