#   Escribir una función que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser:
#   "Hola <Nombre> tienes <Edad> años".

from turtle import clearscreen

clearscreen
import datetime
date = datetime.date.today()
anio=date.year
resultado=int(0)
print("\n")
#nombre=str("tony")
nombre=str(input("Ingresa tu nombre ====> "))
#edad=int(1981)
edad=int(input("¿En que año naciste? => "))

def fn_resultados(edad,anio):
    resultado=int(anio-edad)
    return(resultado)
print("\n")
#print(fn_resultados(edad,anio))
#print("Tienes",fn_resultados(edad,anio))
print(f'Hola {nombre} tienes {fn_resultados(edad,anio)} años')
print("\n\n")