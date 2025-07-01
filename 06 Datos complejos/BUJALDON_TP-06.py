# TP 6 - Estructuras de datos complejas

# 1) Diccionario inicial y agregar frutas nuevas
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Lista de frutas (sin precios)
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)


# 4) Agenda telefónica
agenda = {}
print("\nCargar contactos:")
for _ in range(5):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    agenda[nombre] = numero

consulta = input("¿De quién querés saber el número? ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe.")


# 5) Palabras únicas y contador
frase = input("\nIngresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

# Contador de palabras
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", contador)


# 6) Promedio de notas por alumno
alumnos = {}
for _ in range(3):
    nombre = input("\nNombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# 7) Conjuntos de estudiantes que aprobaron Parcial 1 y 2
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107}

ambos = parcial1 & parcial2
solo_uno = (parcial1 ^ parcial2)
al_menos_uno = parcial1 | parcial2

print("\nAprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# 8) Stock de productos
stock = {
    'Arroz': 10,
    'Fideos': 5,
    'Aceite': 8
}

producto = input("\n¿Producto a consultar? ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. ¿Cuántas unidades tiene el nuevo producto? "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)


# 9) Agenda con tuplas como claves
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:30'): 'Clase de Python',
    ('Viernes', '09:00'): 'Gimnasio'
}

dia = input("\nIngresá el día a consultar: ")
hora = input("Ingresá la hora (formato hh:mm): ")

evento = agenda_eventos.get((dia, hora))
if evento:
    print(f"Actividad agendada: {evento}")
else:
    print("No hay actividad en ese horario.")


# 10) Invertir diccionario país -> capital
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'París',
    'Italia': 'Roma'
}

# Invertimos el diccionario
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("\nDiccionario invertido:", capitales_paises)
