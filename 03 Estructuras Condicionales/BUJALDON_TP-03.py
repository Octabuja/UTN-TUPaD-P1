#Ejercicio 1
edad = int(input("Ingresa tu edad:"))
if edad >= 18:
    print ("Eres mayor de edad")


#Ejercicio 2
nota = int(input("Ingrese su nota"))
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3
num = int(input("ingrese un numero par"))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


#Ejercicio 4
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Eres un niño")
elif 18 > edad >= 12:
    print("Eres adolescente")
elif 30 > edad >= 18:
    print("Eres adulto joven")
else:
    print("Eres adulto mayor")


#Ejercicio 5
contraseña = str(input("Ingrese una clave que contenga entre 8 y 14 caracteres"))
longitud_contra = len(contraseña)
if 8<= longitud_contra <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")


#Ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(moda,mediana,media)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")


#Ejercicio 7
entrada = input("Ingresa una palabra o frase: ")

ultima_letra = entrada[-1].lower()
if ultima_letra in 'aeiou':
    # Si termina con una vocal, agregar el signo de exclamación
    resultado = entrada + '!'
else:
    # Si no termina con una vocal, dejarlo igual
    resultado = entrada
print(resultado)

#Ejercicio 8
entrada = input("Ingrese su nombre")
entrada2 = input("ingrese:"
"1 Si quiere su nombre en mayúsculas PEDRO "
"2 Si quiere su nombre en minúsculas pedro "
"3 Si quiere su nombre con la primera letra mayúscula Pedro")
 
if entrada2 == "1":
    resultado = entrada.upper()

elif entrada2 == "2":
    resultado = entrada.lower()

elif entrada == "3":
    resultado = entrada.title()

else:
    print("El numero ingresado es incorrecto")

print(resultado)


#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto"))

if magnitud<3:
    print("Muy leve (imperceptible)")

elif 3 <= magnitud < 4:
    print("Leve (Ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas pero no causa daños)")

elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")

elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")

else:
    print("Extremo (puede causar graves daños a gran escala)")

print(f"Categoría del terremoto: {magnitud}")


#Ejercicio 10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es del mes? (1-31): "))

# Hemisferio Norte
if hemisferio == 'N': 
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11):
        estacion = "Otoño"
    else:  # Diciembre, enero y febrero
        estacion = "Invierno"
        
# Hemisferio Sur
elif hemisferio == 'S': 
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11):
        estacion = "Primavera"
    else:  # Diciembre, enero y febrero
        estacion = "Verano"
else:
    estacion = "Hemisferio no válido"

# Imprimir el resultado
print(f"Te encuentras en {estacion}.")