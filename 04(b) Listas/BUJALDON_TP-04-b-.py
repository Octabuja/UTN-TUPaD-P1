#Ejercicio1

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Ejercicio2

cosas_favoritas = ["pizza", "libros", "playa", "guitarra", "películas"]
print(cosas_favoritas[-2])

#Ejercicio3

palabras = []
palabras.append("sol")
palabras.append("luna")
palabras.append("estrella")
print(palabras)

#Ejercicio4

animales = ["perro", "gato", "conejo", "vaca"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio5

numeros = [8,15,3,22,7] # Se crea una lista
numeros.remove(max(numeros)) #Con la funcion max() se busca el mayor numero y  con remove se elimina
print(numeros) #Se imprime la lista sin el numero 22


#Ejercicio6

numeros = list(range(10, 31, 5))
print(numeros[:2])

#Ejercicio7

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mustang", "camaro"]
print(autos)

#Ejercicio8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Ejercicio9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan"
compras[0].remove("pan")

print(compras)

#Ejercicio10

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)
