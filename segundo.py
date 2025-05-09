import math

""" nombre = input("¿Cual es tu nombre?")
edad = int(input("¿Cual es tu edad?"))
print(f"la edad de {nombre} es: {edad} \n Adios!") """


""" # calcular IMC
# IMC = = Peso (Kg) / (Estatura (m))^2
peso = float(input("Cual es tu peso?: "))
altura = float(input("Cual es tu altura?: "))
IMC = peso / (altura ** 2)
print(f"tu IMC es: {IMC:.3f}") """

""" #calculadora de descuento
# Descuento = Precio original * (porcentaje de descuento / 100)

precio_original = int(input("¿Cuál es el precio?: "))
descuento = int(input("¿Cuanto descuento tiene?: "))
precio_final = precio_original - (precio_original * (descuento / 100))
print(f"El precio con descuento es: {precio_final:.0f}") """

""" # Promedio de notas
# X = (n1 + n2 + n3) / n
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"el promedio de notas es: {promedio:.1f}")
"""
""" #area de un triangulo
# area = (raiz de 3 / 4 ) * a2
lado = float(input("longitud del lado del triangulo: "))
area = (math.sqrt(3)/4) * (lado **2)
print(f"El area del triangulo es: {area:.1f}") """

df = pd.read_csv("clash_royale_cards.csv")

print("las primeras 5 filas de mi csv")
print(df.head(10))

