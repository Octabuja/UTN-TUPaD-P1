import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que saluda al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones para área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "División por cero"

# 8. Cálculo del IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Conversión Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 10. Cálculo de promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas.")

    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma, resta, producto, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {producto}, División: {division}")

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f}° Fahrenheit.")

    a = float(input("Ingrese el primer número para el promedio: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
