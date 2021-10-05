#a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
#   la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
#c) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó
#   o no la contraseña correctamente, mediante un valor booleano (True o False).

password = '123456'

def manejarContrasenias():
    intentos = 0

    usuario = input('Ingrese contraseña: ')
    while usuario != password:
        
        if intentos != 5:
            usuario = input('Ingrese contraseña: ')
            intentos+=1           
        else:
            print('No se puede seguir ingresando contraseñas')
            usuario = password
            return usuario
    
    if usuario == password:
        print(True)
    else:
        print(False)
    
            
    
manejarContrasenias()
    
    
    

    