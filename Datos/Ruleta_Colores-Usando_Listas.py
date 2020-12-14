# CaosMX
# Dic 2020
# Ex Python Practica

'''
JUEGO: Ruleta de los Colores:
1. El juego pide un color.
2. Si acertamos - Indicar acierto
                - Dar Puntos
                - Pedir otro color
3. Si no acertamos  - Indica error
                    - Dar puntos totales
                    - Fin de l programa

Siguiendo Curso de Python de Manuel Gonzalez: 
https://www.youtube.com/channel/UCQLWbxZbgftDIhw21i6q_OA/featured
https://programarescomounjuego.blogspot.com
'''

colores = ["rojo", "azul", "verde", "blanco", "naranja"]
puntos = 0

print ("----     RULETA DE LOS COLORES     -----")
print ("Adivina los 5 colores: ")
print ("Suma puntos hasta que falles...")

jugando  = True

while jugando:
    color = input("Dime un color: ")
    if color in colores:
        puntos += 1
        print ("Acertaste un color")
        print ("Tienes ", puntos, "puntos")
    else:
        print ("Ese color no esta, Has perdido")
        print ("Conseguiste ", puntos, "puntos")
        jugando = False