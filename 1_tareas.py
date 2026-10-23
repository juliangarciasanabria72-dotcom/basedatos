import asyncio
import time

async def enviar_correo_bienvenida(usuario):
    print(f'[{time.strftime("%X")}] PREPARANDO CORREO PARA {usuario}...')
    await asyncio.sleep(4)
    print(f'[{time.strftime("%X")}] Correo enviado exitosamente a {usuario}...')

async def registrar_usuario(usuario):
    print(f'[{time.strftime("%X")}] Guardando a {usuario} en la BD...')
    await asyncio.sleep(1)
    print(f'[{time.strftime("%X")}] {usuario} guardado en la BD...')
    tarea_correo = asyncio.create_task(enviar_correo_bienvenida(usuario))
    print(f'[{time.strftime("%X")}] Retornando respuesta al frontend: ¡Bienvenido {usuario}!')
    
    return tarea_correo

async def main():
    tarea = await registrar_usuario("juan.perez@sena.edu.co")
    print("El servidor sigue atendiendo...")
    await asyncio.slee(5)

asyncio.run(main())