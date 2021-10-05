from typing import no_type_check, no_type_check_decorator


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculadora():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    inp = int(input("porfavor seleccione una operación: "))
    if inp != 5:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        if inp == 1:
            print(suma(num1,num2))
        elif inp == 2:
            print(resta(num1,num2))
        elif inp == 3:
            print(multiplica(num1,num2))
        elif inp == 4:
            print(divide(num1,num2))
        else:
            print("Caracter no reconocido")
        calculadora()
        
calculadora()



