# Escriba un programa que pida dos números enteros. 
# El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. 
# El programa terminará escribiendo los dos números.


def dosNumeros():
    num1 = int(input('Ingrese primer numero: '))
    num2 = int(input('Ingrese segundo numero: '))

    while num2 < num1:
        num2 = int(input('Ingrese segundo numero: '))

    print('Numero 1:',num1,'| Numero2:',num2)

dosNumeros()