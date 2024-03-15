def ordenar_lista(lista):
    return sorted(lista, reverse=True)

numeros = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
lista_ordenada = ordenar_lista(numeros)
print("Lista ordenada de mayor a menor:", lista_ordenada)