inventario_tienda = [
    {"nombre": "Llanta Trasera Voge 300 DS", "categoria": "Repuestos", "precio": 280000, "stock": 4},
    {"nombre": "Kit Arrastre Suzuki Gixxer 150", "categoria": "Repuestos", "precio": 120000, "stock": 15},
    {"nombre": "Exploradoras LED Dominar 400", "categoria": "Accesorios", "precio": 150000, "stock": 8},
    {"nombre": "Pastillas Freno Gixxer 150", "categoria": "Repuestos", "precio": 45000, "stock": 0},
    {"nombre": "Soporte Celular Aluminio", "categoria": "Accesorios", "precio": 60000, "stock": 3}
]

def procesar_inventarios(productos):
    for producto in productos:
        if producto ["stock"] <=5:
            print(f"¡Alerta!: Stock crititico para: {producto['nombre']}")
        if producto["categoria"] == "Accesorios":
            producto["precio"] = producto["precio"]*0.90
        if producto["stock"]==0:
            print(f"producto agotado:{producto['nombre']}")

            return productos
        

procesar_inventarios(inventario_tienda)