# CaosMX
# Dic 2020
# Ex Python Practica


'''
Comprobar dada una palabra, la cantidad de vocales que contiene:

    Usando el operador in -> Nos dice en determinada posición de un string si el caracter existe en
    otro string predeterminado:

Siguiendo Curso de Python de Manuel Gonzalez: 
https://www.youtube.com/channel/UCQLWbxZbgftDIhw21i6q_OA/featured
https://programarescomounjuego.blogspot.com
'''
#Input
palabra = input ("Dame un una palabra: ")

# String para verificar las vocales
vocales = "aeiouáéíóú"

# Para verificar el caracter en el índice del string:
indice = 0

# Para contar las vocales:
num_vocales = 0

# Recorremos la palabra
while indice <= len(palabra)-1:
    # Si el caracter es una vocal
    if palabra[indice] in vocales:
        # Incremento de contador:
        num_vocales += 1
    # Aumentamos el indice para recorrer el siguiente caracter:
    indice += 1

print ("La cantidad de vocales es: ", num_vocales)