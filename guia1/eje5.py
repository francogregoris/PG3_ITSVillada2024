def palindromos(palabra):
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra: ")
if palindromos(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")
