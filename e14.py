# a)  Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y 
#       devuelva True si el número es una potencia de 2, y False en caso contrario.
# b) Escribir una función que, dados dos números naturales pasados como parámetros, 
#       devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
# (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos,
# descripta en el punto anterior.


def es_potencia_de2(n):
    if n < 1:
        return False
    if n <= 2:
        return True
    i = 2
    while True:
        i *= 2
        if i == n:
            return True
        if i > n:
            return False


def sumaPotencias(n1,n2):
    acumulador=0
    for i in range(n1,n2+1):
        if es_potencia_de2(i):
            acumulador= acumulador+i
        else:
            acumulador
    
    print(acumulador)

sumaPotencias(-1,-5)