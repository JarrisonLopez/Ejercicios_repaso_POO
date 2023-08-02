#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

Tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
Lista = []
for i in range (Tamaño_lista):
    Numero = random.randint(0,100)
    Lista.append(Numero)
print(f"La lista generada es: {Lista}")