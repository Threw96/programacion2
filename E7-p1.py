#Escriba un programa que reciba un nombre y retorne el nombre pasado concatenado 2 veces. 
# Es decir, supongamos que la función se llama duplica, si hacemos duplica(”Federico”)
#el resultado que deberíamos obtener sería: "FedericoFederico".


def duplica(s=''):
    cadena = s*2
    return cadena


print(duplica('Federico'))
