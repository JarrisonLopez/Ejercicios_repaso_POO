#Crear una función que invierta el orden de los elementos en una lista dada.
def main():
    import random
    def invertir_lista(lista):
        return lista[::-1]
    Tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
    Lista = []
    for i in range (Tamaño_lista):
        Numero = random.randint(0,100)
        Lista.append(Numero)
    Lista_invertida = invertir_lista(Lista)
    print(f"La lista original es: {Lista} y la lista invertida es: {Lista_invertida}")
main()