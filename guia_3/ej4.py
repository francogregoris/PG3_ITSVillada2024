resultado = 0
def division(num1, num2):
    resultado = num1 / num2
    print ("la division de los 2 numeros da", resultado)

while True:
    try:
        num1=int(input("ingrese el valor del numero 1 >>"))
        num2=int(input("ingrese el valor del numero 2 >>"))
        division(num1, num2)
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
    except ValueError:
        print("solo se pueden ingresar numeros enteros")
    pregunta=input("seguir diviendo (si/no) ")
    if pregunta != "si":
        break