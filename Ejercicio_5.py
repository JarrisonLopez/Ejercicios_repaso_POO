#Crear una función que convierta grados Fahrenheit a grados Celsius.
def main():
    Fahrenheit = eval(input("Ingrese los grados Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print(f"{Fahrenheit} °F son {round(Celsius,2)} °C ")
main()