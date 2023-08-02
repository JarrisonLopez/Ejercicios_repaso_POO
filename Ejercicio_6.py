#Crear un programa que calcule la suma de los números en una lista dada
import random

Tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
Lista = []
Suma = 0
for i in range (Tamaño_lista):
    Numero = random.randint(0,100)
    Lista.append(Numero)
for i in range (Tamaño_lista):
    Suma = Suma + Lista[i]
print(f"La suma de la lista generada es: {Suma}")