import json
import aiofiles
import asyncio

ARCHIVO_BD = "inventario.json"
db_lock = asyncio.Lock()

async def leer_base_datos():
    try:
        async with aiofiles.open(ARCHIVO_BD, mode="r", encoding="utf-8") as f:
            contenido = await f.read()
            return json.loads(contenido)
    except FileNotFoundError:
        return {"taller": "", "herramientas": []} # Estructura por defecto para evitar errores

async def guardar_base_datos(datos):
    async with aiofiles.open(ARCHIVO_BD, mode="w", encoding="utf-8") as f:
        await f.write(json.dumps(datos, indent=4, ensure_ascii=False))

async def obtener_producto(codigo):
    async with db_lock:
        await asyncio.sleep(0.2)
        datos = await leer_base_datos()
        
        # Verificamos si los datos tienen la clave "herramientas" o si es una lista directa
        herramientas = datos.get("herramientas", []) if isinstance(datos, dict) else datos
        
        for dato in herramientas:
            if dato.get("codigo") == codigo:
                return dato
                
        raise KeyError(f"Producto {codigo} no ha sido encontrado.")

