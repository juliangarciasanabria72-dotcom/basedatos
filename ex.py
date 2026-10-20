nombre_producto="Llantas  pirelli"
precio=430000.00
stock=12
activo=True

print(f"producto{nombre_producto}) | Precio: {precio}")

#2. condiciones

if stock > 0 and activo:
    print("producto disponible para la venta")
elif stock == 0:
    print("Producto agotado")
else:
    print("Producto inactivo")

categorias = ["Lubricantes","Repuestos","Accesorios"]

for categoria in categorias:
    print(f"Revisando la categoria: {categoria}")

#Usamos "def" en lugar de "function" o "() =>"

def caclcular_descuento(precio_base,porcentaje):
    descuento=precio_base*(porcentaje/100)
    return precio_base-descuento

precio_final=caclcular_descuento(precio,10)
print(f"precio con descuento: ${precio_final}")
