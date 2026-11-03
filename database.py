import aiofiles
import json

ARCHIVO_DB = "taller.json"

async def leer_base_datos():
    try:
        async with aiofiles.open(ARCHIVO_DB, mode='r', encoding='utf-8') as f:
            contenido = await f.read()
            if not contenido.strip():
                return []
            return json.loads(contenido)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

async def guardar_base_datos(datos):
    async with aiofiles.open(ARCHIVO_DB, mode='w', encoding='utf-8') as f:
        await f.write(json.dumps(datos, indent=4, ensure_ascii=False))