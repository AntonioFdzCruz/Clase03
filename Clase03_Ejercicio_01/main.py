# Escribir una funcion que reciba un mensaje y un nombre, y escriba en pantalla "<mensaje> <nombre>"

from turtle import clearscreen

clearscreen

print('\n')
yourname=str(input('¿Cómo te llamas? ■ '))
yourmessage=str(input('¿Cuentame como va tu día? ■ '))
print('\n')
print(f'Hola ',yourname)
print(f'Es interesante lo que me platicaste => ', yourmessage)
print('Gracias y que sigas teniendo un excelente día')
print('\n')

def fn_datos(nombre:str,mensaje:str):
    return(nombre,mensaje)

print("Función |First your typed NAME & SECOND print the MESSAGE input|=>\n ",fn_datos(yourname,yourmessage))
print('\n')
