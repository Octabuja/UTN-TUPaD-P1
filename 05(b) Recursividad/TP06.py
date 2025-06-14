# TP de Recursividad - Programación I

# 1. Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2. Serie de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4. Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# 5. Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6. Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7. Contar bloques en pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8. Contar ocurrencias de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)


# Programa principal de prueba
if __name__ == "__main__":
    print("1) Factorial:")
    num = int(input("Ingrese un número para calcular sus factoriales: "))
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

    print("\n2) Serie de Fibonacci:")
    n = int(input("Ingrese hasta qué posición mostrar la serie de Fibonacci: "))
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

    print("\n3) Potencia recursiva:")
    base = int(input("Base: "))
    exp = int(input("Exponente: "))
    print(f"{base}^{exp} = {potencia(base, exp)}")

    print("\n4) Decimal a binario:")
    dec = int(input("Ingrese un número decimal: "))
    binario = decimal_a_binario(dec)
    print(f"Binario: {binario if binario else '0'}")

    print("\n5) Palíndromo:")
    palabra = input("Ingrese una palabra: ").lower()
    print("Es palíndromo:", es_palindromo(palabra))

    print("\n6) Suma de dígitos:")
    numero = int(input("Ingrese un número: "))
    print("Suma de dígitos:", suma_digitos(numero))

    print("\n7) Contar bloques en pirámide:")
    nivel = int(input("Cantidad de bloques en el nivel más bajo: "))
    print("Total de bloques:", contar_bloques(nivel))

    print("\n8) Contar dígitos:")
    n = int(input("Ingrese un número: "))
    d = int(input("Ingrese el dígito a contar: "))
    print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")
