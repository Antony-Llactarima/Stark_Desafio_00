# Impresion de los datos

def print_nombre(descripcion, valor):
    print(f"{descripcion}: {valor}")

def print_nombre_altura(nombre, altura):
    print(f"Nombre: {nombre} | Altura: {altura}")

def print_altura_promedio(altura_promedio):
    print(f"Altura promedio de los superheroes: {altura_promedio}")


# Funciones que realizan los ejercicios
# B
def nombre_superhores(lista_super):
    for i in range(len(lista_super)):
        print_nombre("Nombre", lista_super[i]["nombre"])

# C
def obtener_nombre_altura(lista_super):
    for i in range(len(lista_super)):
        print_nombre_altura(lista_super[i]["nombre"], lista_super[i]["altura"])

def determinar_max_altura(lista_super)->list:
    for i in range(len(lista_super)):
        altura = float(lista_super[i]["altura"])
        if i == 0:
            nombre_max_altura = lista_super[i]["nombre"]
            max_altura = float(lista_super[i]["altura"])
        elif altura > max_altura:
            nombre_max_altura = lista_super[i]["nombre"]
            max_altura = float(lista_super[i]["altura"])
    super_max_altura = [nombre_max_altura, max_altura]
    return super_max_altura

# D
def determinar_min_altura(lista_super):
    for i in range(len(lista_super)):
        altura = float(lista_super[i]["altura"])
        if i == 0:
            nombre_min_altura = lista_super[i]["nombre"]
            min_altura = float(lista_super[i]["altura"])
        elif altura < min_altura:
            nombre_min_altura = lista_super[i]["nombre"]
            min_altura = float(lista_super[i]["altura"])
    super_min_altura = [nombre_min_altura, min_altura]
    return super_min_altura

# E
def informar_altura_promedio(lista_super):
    total_personajes = len(lista_super)
    peso_total = 0
    for i in range(total_personajes):
        peso_total = peso_total + float(lista_super[i]["altura"])
    print_altura_promedio(peso_total / total_personajes)

# F
def informar_max_min_altura(max_personaje, min_personaje):
    print(f"El personaje con mayor altura:\nNombre: {max_personaje[0]} | Altura {max_personaje[1]}")
    print(f"El personaje con menor altura:\nNombre: {min_personaje[0]} | Altura {min_personaje[1]}")

# G
def calcular_informar_peso(lista_super):
    for i in range(len(lista_super)):
        peso = float(lista_super[i]["peso"])
        if i == 0:
            nombre_max_peso = lista_super[i]["nombre"]
            max_peso = float(lista_super[i]["peso"])
        elif peso > max_peso:
            nombre_max_peso = lista_super[i]["nombre"]
            max_peso = float(lista_super[i]["peso"])
    
    print(f"Personaje con mayor peso:\nNombre: {nombre_max_peso} | Peso: {max_peso}")
    
    for i in range(len(lista_super)):
        peso = float(lista_super[i]["peso"])
        if i == 0:
            nombre_min_peso = lista_super[i]["nombre"]
            min_peso = float(lista_super[i]["peso"])
        elif peso < min_peso:
            nombre_min_peso = lista_super[i]["nombre"]
            min_peso = float(lista_super[i]["peso"])
    print(f"Personaje con menor peso:\nNombre: {nombre_min_peso} | Peso: {min_peso}")
