#Crear un programa que genere una matriz de números y la imprima en pantalla.
import random

num_filas = int(input("Ingrese numero de filas: "))
num_columnas = int(input("Ingrese numero de columnas: "))

matriz = [[random.randint(1, 100) for _ in range(num_columnas)] for _ in range(num_filas)]

for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()
