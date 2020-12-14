# CaosMX
# Dic 2020
# Ex Python Practica

'''
Tuplas: Estructura con tipos de datos que contienen mas de 1 elemento
Ej: (15, "hola, True, (1,2,3))
Las tuplas se pueden contatenar: t3 = t1 +t2
Se puede utilizar el operador de indexación para saber que tiene en su índice: t3[2]
Puede tener un solo elemento: (5,)
Se puede usar len para saber la longitud dela tupla
Las tuplas son tipos de datos secuencia
Son inmutables

Siguiendo Curso de Python de Manuel Gonzalez: 
https://www.youtube.com/channel/UCQLWbxZbgftDIhw21i6q_OA/featured
https://programarescomounjuego.blogspot.com
'''

#Crear tupla a partir de las siguientes 3 listas de animales para ver las mascotas de la lista:
mamiferos = ("tigre", "gato", "leon")
aves = ("aguila", "buitre", "canario")
reptiles = ("tortuga", "serpiente")

#Tenemos que tomar los segmentos, sino concatenaría los caracteres "gatocanariotortuga":
mascotas = mamiferos[1:2] + aves[2:] + reptiles[0:1]
print (mascotas)

#Declarando los elementos como tupla:
mascotas2 = (mamiferos[1], aves[2], reptiles[0])
print (mascotas2)

#Declarando cada elemento como tupla: 
mascotas3 = (mamiferos[1],) + (aves[2],) + (reptiles[0],)
print (mascotas3)
