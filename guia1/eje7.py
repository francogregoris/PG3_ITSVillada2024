def numerostep(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if abs(int(numero_str[i]) - int(numero_str[i+1])) != 1:
            return False
    return True

numero = int(input("Ingrese un número: "))
if numerostep(numero):
    print(f"{numero} es un número step")
else:
    print(f"{numero} no es un número step")