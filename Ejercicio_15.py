# Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    return cadena == cadena[::-1]
entrada_usuario = input("Ingresa una cadena de texto: ")

if es_palindromo(entrada_usuario):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
