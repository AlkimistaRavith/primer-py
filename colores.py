colores_rgb = {
    "rojo" : "#ff0000", 
    "azul" : "#0096d2" ,
    "verde" : "#00bb2d"
}

colores_2 = {
    "blanco" : "#ffffff" ,
    "negro" : "#000000" ,
    "rojo" : "rojo"
}

print(colores_rgb)

colores_rgb["verde reseda"] = "#587246"

print(colores_rgb)

colores_rgb["verde"] = "verde"

print(colores_rgb)

del colores_rgb["verde reseda"]

print(colores_rgb)

eliminado = colores_rgb.pop("verde")

print(eliminado)
print(colores_rgb)

colores_2.update(colores_rgb)

print(colores_2)
print(colores_rgb)

print(colores_rgb.values)