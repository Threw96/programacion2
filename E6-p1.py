#Escriba un programa que calcule e imprima el resultado de la suma de los números 
# naturales mayores que n y menores que m usando una función recursiva.

# entrada: n=5, m=10; salida: 45
def sumaNaturales(n, m):
    sum = n
    if sum >= m:
        return sum
    else:
        return sum + sumaNaturales(sum + 1, m)


print(sumaNaturales(5,10))