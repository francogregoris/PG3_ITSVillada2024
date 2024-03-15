def buscaradentro(lista, elemento):
    #funcion con los parametros a pedir
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return "El elemento no se encuentra en la lista."
        #esto es para leer la lista,compararla y ver si el elemento esta en la lista
lista = [8, 12, 9, 45]
#esta es la lista precreada
ele_buscado = 12
resultado = buscaradentro(lista, ele_buscado)
print("El elemento", ele_buscado, "se encuentra en el índice", resultado)
#compara el numero pedido con la funcion 
