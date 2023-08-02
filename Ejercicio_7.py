#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
import random

Tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
Lista = []
for i in range (Tamaño_lista):
    Numero = random.randint(0,100)
    Lista.append(Numero)
Mas_grande = max(Lista)
Mas_pequeño = min(Lista)
print(f"El numero mas grande de la lista es: {Mas_grande} y el numero mas pequeño es: {Mas_pequeño}")