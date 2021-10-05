# Escriba un programa que reciba un nombre y un númeron, y retorne el nombre pasado concatenado n veces. 
# Es decir, supongamos que la función se llama duplica, si hacemos
# duplica(”F ederico”, 3) el resultado que deberíamos obtener sería: "FedericoFedericoFederico"


def multiplica(string='',n=1):
    cadena = string*n
    return cadena

print(multiplica("juan",3))