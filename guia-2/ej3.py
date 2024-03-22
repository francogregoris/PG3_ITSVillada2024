class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # ingreso de los lados del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        # Encuentra el lado mayor
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", lado_mayor)

    def es_equilatero(self):
        # Verifica si todos los lados son iguales
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return True
        else:
            return False



# pide al usuario que ingrese las longitudes de los lados del triángulo
lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))


triangulo = Triangulo(lado1, lado2, lado3)

# Llama al método imprimir_lado_mayor para imprimir el lado más largo del triángulo
triangulo.imprimir_lado_mayor()

# Verifica si el triángulo es equilátero y muestra un mensaje correspondiente
if triangulo.es_equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")