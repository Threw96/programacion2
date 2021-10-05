#primeros 25 numeros pares
def naturales25(n=0,contador=25):
    if contador == 0:
        return
    elif (n % 2) == 0:
        print(n)
        naturales25(n+1, contador-1)
    else:
        naturales25(n+1, contador)
    

#naturales25()

#Imprimir n números naturales pares 
# naturalesN: int -> string
#toma un numero
#devuelve los numeros pares hasta ese numero
#entrada: 10, salida: "0,2,4,6,8,10"
#entrada: 20, salida: "0,2,4,6,8,10,12,14,16,18,20"
#entrada: 5, salida: "0,2,4"

n = int (input ("Ingrese un número "))
def naturalesN (n):
    if 0 == n:
        print (n)
    else:
        if (n % 2) == 0:
            print (n)
            naturalesN (n - 1)
        else:
            naturalesN (n - 1)

naturalesN(n)
