class Persona:
    def __init__(self) :
        self.nombre = input("Ingrese un nombre ")
        self.edad = int(input("Ingrese una edad "))

    def imprimir(self):
        print("nombre",self.nombre)
        print("edad",self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo"))


    def pagar_impuestos(self):
        self.imprimir() 
        if self.sueldo > 3000:
            print("El empleado", self.nombre, "debe pagar impuestos.")
        else:
            print("El empleado", self.nombre, "no debe pagar impuestos.")

empleado = Empleado()
empleado.pagar_impuestos()