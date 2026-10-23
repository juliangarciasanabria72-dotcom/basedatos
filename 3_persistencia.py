import asyncio
import aiofiles
import json 

inventario = [
    {"codigo": "PEP01","nombre":"Llanta rin 17","stock":10},
    {"codigo":"PEP02","nombre":"Aceite Motul 7100","stoc":5}
    
]


async def guardar_inventario(datos,archivo):
    print("Guardando datos de forma asincrona")
    async with aiofiles.open(archivo,mode="w",encoding='uft-8')as f:
        texto_json=json.dumps(datos,indent=4)
        await f.write(texto_json)
        print("inventario guardado en el disco")


async def cargar_inventario(archivo):
    print("cargando los datos el Json...")
    try:
        async with aiofiles.open(archivo, mode="r", encoding='utf-8') as archivo_json:
            texto_json=await archivo_json.read()
            datos = json.loads(texto_json)
            return datos
    except FileNotFoundError:
        print("El archvo no existe. Iniciando con inventario vacio")
        return[]

    async def main():
        await guardar_inventario(inventario,'inventario.json')

        datos_recuperados=await cargar_inventario('inventario.json')
        print("Datos recuperados:", datos_recuperados)

    asyncio.run(main())

