meses =  (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)
try:
    numero=int(input("decime un numero de mes "))
    mes = meses[numero - 1 ]
    print ("me dijiste el mes", mes)
except IndexError:
    print("el numero ingresado no es un mes")