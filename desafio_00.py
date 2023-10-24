from data_stark2 import lista_personajes
from funciones_desafio_00 import *
# Desafío #00:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

continuar = True

personaje_max_altura = ""
personaje_min_altura = ""

while continuar:
    print("""
****************************************************************
Menu Principal

A. Mostrar nombres de superheroes.
B. Mostrar nombre y altura de superheroes.
C. Determinar superheroe mas alto.
D. Determinar superheroe mas bajo.
E. Mostrar el promedio de altura de los superheores.
F. Mostrar los superheroes mas y menos altos.
G. Mostrar los superheores mas y menos pesados.
S. Salir
****************************************************************
""")
    opcion = input("Ingrese su opcion: ").upper()
    
    match opcion:
        case "A":
            nombre_superhores(lista_personajes)
        case "B":
            obtener_nombre_altura(lista_personajes)
        case "C":
            personaje_max_altura = determinar_max_altura(lista_personajes)
            print("Personaje con mayor altura determinado.")
        case "D":
            personaje_min_altura = determinar_min_altura(lista_personajes)
            print("Personaje con menor altura determinado")
        case "E":
            informar_altura_promedio(lista_personajes)
        case "F":
            if type(personaje_max_altura) == list and type(personaje_min_altura) == list:
                informar_max_min_altura(personaje_max_altura, personaje_min_altura)
            else:
                print("Aun no se ha determinado cual es el superheroe mas alto o bajo")
        case "G":
            calcular_informar_peso(lista_personajes)
        case "S":
            continuar = False
        case _:
            print("Error... Opcion no valida, reintentelo")

