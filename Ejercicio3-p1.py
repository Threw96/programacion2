#Imprimir los n numeros naturales pares mayores que m
# naturalesN2: int, int -> string
#toma dos numeros n y m respectivamente
#devuelve los n nunmeros pares mayores que m
#entrada: 10,50 ; salida: "52,54,56,58,60,62,64,66,68,70"
#entrada: 5,20 ; salida: "22,24,26,28,30"
#entrada: 2,2 ; salida: "4,6"

n = int (input ("Ingrese el valor de n "))
m_numero = int (input ("Ingrese el valor de m "))
m = m_numero + 1    

def naturalesN2 (n, m, contador = 0):
    if contador == n:
        return
    elif (m % 2) == 0:
            print (m)
            naturalesN2 (n, m + 1, contador + 1)
    else:
            naturalesN2 (n, m + 1, contador)
        
naturalesN2(n, m)