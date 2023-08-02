#Crear un programa que genere una lista de números pares entre 1 y 100.
import random
Lista = []
for i in range(2,101,2):
    Lista.append(i)
print(f"La lista de numeros pares entre 1 a 100 es: {Lista}")