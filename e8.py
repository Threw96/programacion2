#Nos piden que escribamos una función que le pida al usuario que ingrese un
# número positivo. Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar
# de su error mediante un mensaje y volverle a pedir el número.

def validar():
    num = int(input('Ingrese un numero positivo: '))
    while num < 0 :
        print('El dato ingresado no es un numero positivo!!!')
        num = int(input('Ingrese un numero positivo: '))

validar()
