
#Ejercicio 1 
#Imprimir números del 0 al 100 en orden creciente, mostrando uno por línea:
for i in range(101):
   print(i)


#Ejercicio 2
#Determinar la cantidad de dígitos de un número entero ingresado por el usuario:
numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))  # Usamos abs para manejar números negativos
print(f"El número tiene {cantidad_digitos} dígitos.")


#Ejercicio 3
#Sumar los números entre dos valores dados por el usuario, excluyendo esos dos valores:
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
suma = sum(range(inicio + 1, fin))  # Excluye los extremos
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")


#Ejercicio 4
#Sumar números ingresados por el usuario hasta que ingrese un 0:
total = 0
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")


#Ejercicio 5
#Juego para adivinar un número aleatorio entre 0 y 9:
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Acertaste! El número era {numero_aleatorio}. Intentos: {intentos}")
        break
    else:
        print("Intenta de nuevo.")


#Ejercicio 6
#Imprimir los números pares entre 0 y 100 en orden decreciente:
for i in range(100, -1, -2):  # Inicia en 100, va hasta 0, con paso -2
    print(i)


#Ejercicio 7
#Calcular la suma de todos los números entre 0 y un número entero positivo indicado por el usuario:
numero = int(input("Ingresa un número entero positivo: "))
suma = sum(range(1, numero + 1))  # Suma de 1 hasta el número ingresado
print(f"La suma de los números entre 0 y {numero} es: {suma}")


#Ejercicio 8
#Contar cuántos números son pares, impares, negativos y positivos entre 100 números ingresados:
# Cantidad de números que se van a ingresar
CANTIDAD_NUMEROS = 100  # Podés cambiar esto a un número menor para pruebas

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#Ejercicio 9
#Calcular la media de 100 números enteros ingresados:
# Cantidad de números que se van a ingresar
CANTIDAD_NUMEROS = 100  # Podés cambiar este valor para probar

suma_total = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero

media = suma_total / CANTIDAD_NUMEROS

print(f"\nLa media de los {CANTIDAD_NUMEROS} números ingresados es: {media}")


#Ejercicio 10
#nvertir el orden de los dígitos de un número ingresado por el usuario:
numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]  # Se invierte el string
print(f"El número invertido es: {numero_invertido}")
