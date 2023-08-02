#Escribir una función que calcule el factorial de un número dado
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

Numero = int(input("Ingrese el numero: "))
factorial_resultado = factorial(Numero)
print(f"El factorial de {Numero} es: {factorial_resultado}") 
