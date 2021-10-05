# Usando la función, dada como ejemplo en la presentación de La Receta en Python, para convertir una 
# temperatura en Fahrenheit a Celsius se pide que genere una tabla de
# conversión de temperaturas, desde 0◦F hasta 120◦F, de 10 en 10.

#Representamos temperaturas mediante números enteros
2 #farCel: Int -> Int
3 #El parámetro representa una temperatura en Fahrenheit y,
4 # se retorna su equivalente en Celsius.
5 # entrada: 32, salida: 0
6 # entrada: 212, salida: 100
7 # entrada: -40, salida: -40

def farCel():
    f=32
    for i in range(0,120+1):
        value = (f-32)*5/9
        f+=10
        print(value)

farCel()