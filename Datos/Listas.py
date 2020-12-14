# CaosMX
# Dic 2020
# Ex Python Practica

'''
Listas
Podemos hacer las mismas operaciones que con las cadenas de caracteres y con las tuplas, 
pero estas si podemos editarlas.
Agregar, Eliminar, Cambiar


Siguiendo Curso de Python de Manuel Gonzalez: 
https://www.youtube.com/channel/UCQLWbxZbgftDIhw21i6q_OA/featured
https://programarescomounjuego.blogspot.com
'''

mascotas = ["gato", "perro", "canario", "cocodrilo"]
print (mascotas)

#Modificando el índice 3 (4o elemento)
mascotas[3] = "tortuga"
print (mascotas)

# Hay que elegir correctamente Listas o Tuplas:
# Las tuplas son mas rápidamente accesibles
# Las listas son mas versátiles

# Crear secuencias entre elementos como tuplas o listas según convenga:
dias_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

dias_entrenamiento = ["Lunes", "Miercoles", "Viernes"]

print (dias_semana)
print (dias_entrenamiento)

'''
('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
['Lunes', 'Miercoles', 'Viernes']
'''

# Creando una lista del 1 al 100 usando WHILE a partor de una lista vacía:

lista = []
n = 1

while n <= 100:
    lista = lista +[n]
    n += 1
print (lista)