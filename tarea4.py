#"codigo","telefono","detalle","precio"

productos = [
    ["001","Huawei10","nuevo",100000], 
    ["002","Motorola7.0","nuevo",500000],
    ["003","Galaxy02","usado",150000],
    ["004","iphone","reacondicionado",789000]
]

codigo = input("agregue nuevo codigo: ")
telefon = input("agregue marca del teléfono: ")
detalle = input("agregue su estado (detalle): ")
precio = input("agregue su precio de venta: ")

nuevo = [codigo,telefon,detalle,precio]

productos.append(nuevo)

#modificar
productos[0][2] = "dañado"

#eliminar
productos.pop(1)

print(productos)