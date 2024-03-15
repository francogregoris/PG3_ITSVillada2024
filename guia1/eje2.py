def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    #se encarga de al anio ingresado compararlo con los requisitos y ver si cumple con estos 
anio = int(input("Ingrese un año: "))
if es_bisiesto(anio):
    print(f"{anio} es bisiesto")
else:
    print(f"{anio} no es bisiesto")
    #esto nos imprime el resultado de la anterior comparacion