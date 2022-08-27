#   Escribir una función que reciba el año actual y el año de nacimiento, usando la funcion anterior 
#   enviando esta como argumento obtenga el mensaje:
#   "Hola <Nombre> tienes <Edad> años".

from turtle import clearscreen

clearscreen
#import datetime
#date = datetime.date.today()
#anio=date.year
resultado=int(0)
print("\n")
#nombre=str("tony")
nombre=str(input("Ingresa tu nombre =====> "))
#edad=int(1981)
edad=int(input("¿En que año naciste? ==> "))
anio=int(input("Escribe el año actual => "))

def fn_resultados(edad,anio):
    resultado=int(anio-edad)
    return(resultado)
print("\n")
#print(fn_resultados(edad,anio))
#print("Tienes",fn_resultados(edad,anio))
#print(f'Hola {nombre} tienes {fn_resultados(edad,anio)} años')
argumento_01=str(nombre)
argumento_02=str(fn_resultados(edad,anio))
print(f'Hola {argumento_01} tienes {argumento_02} años')
print("\n\n")
