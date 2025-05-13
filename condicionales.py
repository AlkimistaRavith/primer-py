

""" # if - else

edad = int(input(f"indicar edad: "))

if edad >= 40 :
    print("entra gratis")
elif edad >= 18 :
    print("debe pagar entrada")
else :
    print("no pasa")
 """

## iteradores
""" 
lista = range(20)

for index in lista :
    print(f"iteración: {index}")

print(lista)
 """

""" 
diccionario = {
    "color1" : "amarillo" ,
    "color2" : "rojo" ,
    "color3" : "azul"
}

for clave, valor in diccionario.items():
    print(f"clave: {clave} , valor: {valor}")
 """

contador = 3

while contador > 0 :
    print("imprime algo")
    contador = contador - 1