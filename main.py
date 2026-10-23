from fastapi import FastAPI, HTTPException #FastAPI = framework
from database import leer_base_datos, obtener_producto, guardar_base_datos
from schemas import productoCreate
appiRest = FastAPI(
    title="API inventarios SENA",
    description="Mi primera API asincrona",
    version="1.0.0"
)

# endpoints = direccion donde se reciben las peticiones
# Peticiones = solicitar el procesamiento de un metodo
# metodo = get, POST, Put, Delete

@appiRest.get("/") # Decorador -> Funcion que recibe como parametro otra funcion
async def ruta_principal():
    return {"mensaje": "Bienvenido a mi primera API Rest"}

@appiRest.get("/estado")
async def estado_servidor():
    return {"status": "En linea", "Servicios": "operativos Sin ningun inconveniente"}

@appiRest.get("/suma")
async def valor_suma(num1: int, num2: int):
    resultado = num1 + num2
    return {"suma": resultado}

@appiRest.get("/prodocutos")
async def listar_productos():
    datos = await leer_base_datos()
    return {"cantidad": len(datos), "productos": datos}

@appiRest.get("/productos/{codigo_producto}")
async def buscar_un_producto(codigo_producto: str):
    try:
        producto = await obtener_producto(codigo_producto)
        return producto
    except KeyError:
        raise HTTPException(status_code=404, detail="El producto solicitado no existe en la BD")

@appiRest.get("/categorias")
async def obtener_categorias():
    datos = await leer_base_datos()
    
    herramientas = datos.get("herramientas", []) if isinstance(datos, dict) else datos
    
    categorias = list(set(h.get("categoria") for h in herramientas if "categoria" in h))
    
    return categorias

@appiRest.post("/productos", status_code=201)
async def registrar_nuevo_producto(producto: productoCreate):
    datos = await leer_base_datos()
    for dato in datos:
        if dato["codigo"] == producto.codigo:
            raise HTTPException(status_code=400, detail="El producto ya existe en la base de datos")
            
    nuevo_producto = producto.model_dump()
    datos.append(nuevo_producto)
    await guardar_base_datos(datos)

    return {"mensaje": "Producto registrado exitosamente", "producto": nuevo_producto}

@appiRest.put("/productos/{codigo_producto}")
async def actualizar_producto(codigo_producto: str, producto_actualizado: productoCreate):
    datos = await leer_base_datos()
    for posicion, dato in enumerate(datos):
        if dato["codigo"] == codigo_producto:
            datos[posicion] = producto_actualizado.model_dump()
            datos[posicion]["codigo"] = codigo_producto
            await guardar_base_datos(datos)
            return {"mensaje": "Producto actualizado exitosamente", "producto": datos[posicion]}
