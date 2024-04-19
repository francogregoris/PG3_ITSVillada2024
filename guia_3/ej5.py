try:
    with open("archivo.txt", "w") as archivo:
        archivo.write(123)
except TypeError:
    print("no se puede escribir un entero en un archivo de texto.")