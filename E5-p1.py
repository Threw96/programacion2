#1+2=3+3=6+4=10+5=15+6=21+7=28+8=36+9=45+10=10

valor=int(input('Ingrese n numeros para sumar '))

def sumaNaturales(n = 1, c = 0, s = 0):
    
    if c != valor:
        s = s + n
        sumaNaturales(n + 1, c + 1, s)
    else:
        print (s)

sumaNaturales()