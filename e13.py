#Escriba una función que reciba un número natural e imprima todos los números
# primos que hay hasta ese número. Para esto se pide que:
#a) Defina una función es_primo que toma un número natural y verifique si es un número primo.
#b) Resuelva el problema usando la función definida en el punto anterior.

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primos(n):
    for i in range(1,n+1):
        if es_primo(i) is True:
            print(i)
    


primos(19)
        