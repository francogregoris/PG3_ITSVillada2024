def contar_vocales(frase):
    vocales = "aeiou,AEIOU"
    cant_vocales = 0
    for letra in frase:
        if letra in vocales:
            cant_vocales += 1
    return cant_vocales

frase = input("Ingrese una palabra: ")
print("Ls cantidad de vocales es :", contar_vocales(frase))
