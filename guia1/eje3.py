def asd(ancho, alto, caracter):
    for _ in range(alto):
        print(caracter * ancho)

ancho = int(input("Ancho: "))
alto = int(input("Alto: "))
caracter = input("Caracter: ")
asd(ancho, alto, caracter)