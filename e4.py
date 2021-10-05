# Escribir una función que tome un una cantidad m de valores que son ingresados 
# por el usuario y, en la medida que lo ingresa, se muestra el factorial de ese número. El valor de
# m es ingresado inicialmente por el usuario.

def factorizar():
    number = int(input('Ingrese un numero m: '))
    factorial = 1
    if number < 0:
        print('El factorial de un numero negativo no exite')
    elif number == 0:
        print('El factorial de 0 es 1')
    else:
        for i in range (1,number + 1):
            factorial = factorial * i
        print('El factorial del numero ', number,' es: ',factorial)
    factorizar()

factorizar()
