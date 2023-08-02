#Escribir una función que calcule la media aritmética de una lista de números
import random

Tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
Lista = []
for i in range (Tamaño_lista):
    Numero = random.randint(0,100)
    Lista.append(Numero)

def calcular_media_aritmetica(lista_numeros):
    suma = sum(lista_numeros)
    cantidad_elementos = len(lista_numeros)
    media = suma / cantidad_elementos
    return media

media_resultado = calcular_media_aritmetica(Lista)
print(f"La media aritmética de la lista es: {media_resultado}")
