# CaosMX
# Dic 2020
# Ex Python Practica

'''
Range = Secuencia de números enteros almacenados como intervalo
    >>> range (10)
            range (0,10)
    >>> 5 in range (10)
            True
    >>> 10 in range (10)
            False 

Se le puede pasar inicio, fin e incluso un tercer argumento que es el salto:
    >>> range (2, 20, 2)
            2, 4, 6, ...


Siguiendo Curso de Python de Manuel Gonzalez: 
https://www.youtube.com/channel/UCQLWbxZbgftDIhw21i6q_OA/featured
https://programarescomounjuego.blogspot.com
'''

a = range (1, 11)
print (a)

#Programa que pida un numero entero que esté en el intervalo del 18 al 25 
# y que siga pidiendo números mientras nos mantengamos en ese intervalo, 
# usando el tipo range:

n = int (input ("Teclea un # entre el 18 y 25: "))

while n in range (18, 26):
    print ("En rango...")
    n = int (input ("Teclea un # entre el 18 y 25: "))
else:
    print ("Fuera de rango...")

'''
Teclea un # entre el 18 y 25: 22
En rango...
Teclea un # entre el 18 y 25: 24
En rango...
Teclea un # entre el 18 y 25: 30
Fuera de rango...
'''
