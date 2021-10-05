# Calcular e imprimir el resultado de la suma de los primeros 
# 50 numeros naturales 
# sumaNaturales: none -> int
# no toma ningun valor
#devuelve la suma de los primeros 50 naturales
# entrada: none ; salida: 1275

def sumaNaturales(n = 1, c = 0, s = 0):
    if c != 50:
        s = s + n
        sumaNaturales(n + 1, c + 1, s)
    else:
        print (s)

sumaNaturales()