#Escriba una función que reciba una cantidad de pesos, una tasa de interés y un
# número de años y retorne, como resultado, el monto final a obtener. La fórmula a utilizar es:
#Cn = C *(1 + x/100)*n
# Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

# Representamos el peso en valor numero
# c = capital inicial
# x = tasa de interes
# n = numeros de años a calcular.

c = int(input('Ingrese capital inicial: '))
x = int(input('Ingrese tasa de interes: '))
n = int(input('Ingrese numero de años a calcular: '))

def valorPeso():
    for i in range(0,n+1):
        value = c * (1 + x/100) * n
    print('El valor del capital: ',c,', con tasa de interes de: ',x,'%'+' dentro de: ',n,'años es de: ',value)

valorPeso()