def suma():
    while True:
        try:
            num1 = int(input("Ingresa un número: "))
            num2 = int(input("Ingresa otro número: "))

            suma = num1 + num2

            print("La suma de", num1, "y", num2, "es:", suma)

            continuar = input("¿Quiere seguir sumando valores? (si/no): ")

            if continuar.lower() != 's':
                break

        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")

suma()