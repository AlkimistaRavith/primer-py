# Tipos de datos en python


### lisa de datos

lista_de_numeros = [1,2,3,4,5,6,7,8,9]

frutas = ['manzana','banana','pera',True,[1,2,3,[4,5,6]]]

#modificar lista

frutas[3] = 'uva'
frutas[2] = 'naranja'

#append: agrega un item al final
frutas.append('kiwi')

frutas.insert(2, 'pera')

""" print(frutas)

#tamaño de la lista o algo más
print(len(frutas)) 
"""

#pop y remove para eliminar (buscar)


#diccionarios

persona = {
    "nombre": "juan" ,
    "edad": 35 ,
    "ciudad": "Hualpen" ,
    "cursos": ["html","css","js"]
}

#acceso


""" 
#modificar
persona["ciudad"] = "Santiago"
print(persona)

persona["rut"] = 17389651-4

del persona["rut"]
print(persona) 
"""

#sets, similar a dict. no muestra repetidos
##funcionan como conjuntos, y sus operaciones

numeros = {1,2,3,4,5,6,7,8,9,4}

numeros.add(22)
numeros.remove(22)
""" 
print(numeros)
 """

#tuplas inmutables (no se puede modificar despues de crear)

colores = ("rojo","verde","azul")

print(colores)

print(colores[1])

