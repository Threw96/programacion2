# Escriba un programa que permita al usuario ingresar un conjunto de notas, 
# preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente,
# al finalizar la toma de datos.


def promedio():
    nota = int(input('Ingrese una nota: '))
    contador = 1
    acumulador = nota

    condicion = input('Desea seguir ingresando notas? Y/N: ')
    while condicion == 'Y':
        nota = int(input('Ingrese una nota: '))
        condicion = input('Desea seguir ingresando notas? Y/N: ')
        contador+=1
        acumulador = acumulador + nota

    promediado = acumulador / contador

    print('La nota promoediada fue de : ',promediado)       

promedio()
