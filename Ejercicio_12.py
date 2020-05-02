def salario():
    #Horas por dia
    hpd =  int(input("Ingrese las horas por dia del empleado: "))
    
    if hpd > 0 and hpd <= 8:
        #Tarifa por hora
        tph = float(input("Ingrese tarifa por hora: "))
        d = int(input("Ingrese el número de dias que laboró: "))
        
    else:
        print("El empleado debe tener más de cero horas y menos de ocho, intente de nuevo, por favor.\n")
        return salario()
    
    Pago = (hpd*tph)*d
    print("Su pago es de:","{:.2f}".format(Pago),"pesos")
    #Volver a intentar
    x = int(input("\nSeleccione 1 si quiere voler a intentar, cualquier otro número para salir: "))
    if x == 1:
        return salario()
    else:
        print("\t\t¡Gracias!")

print("\t\t Pago")
salario()
