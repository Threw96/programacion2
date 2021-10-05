#Escriba una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, 
# que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea
# mayor que el segundo.
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

# entrada: 3 y 9, salida: 3
# entrada: 2 y 16, salida: 8

def numerosfor(n, m):
    count = 0
    for i in range(n, m):
        if (n*(i-n)) < m:
            count += 1
    return count

def numeroswhile(n, m):
    x = n
    count = 1
    while n < m:
        count += 1
        n += x
    return count

print(numeroswhile(2,16))