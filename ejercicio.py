import asyncio
import json
import time

async def monitorear_sistema():
    """Corrutina que imprime el estado del sistema cada 2 segundos en un bucle infinito."""
    while True:
        print(f"[{time.strftime('%X')}] Monitor: Sistema funcionando OK...")
        await asyncio.sleep(2)

async def hacer_backup():
    """Corrutina que intenta leer 'inventario.json', simula lentitud y guarda 'backup.json'."""
    print(f"[{time.strftime('%X')}]  Iniciando proceso de respaldo de datos...")
    await asyncio.sleep(1.5)
    
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo_origen:
            datos = json.load(archivo_origen)
        
        with open("backup.json", "w", encoding="utf-8") as archivo_destino:
            json.dump(datos, archivo_destino, indent=4)
            
        print(f"[{time.strftime('%X')}]  Backup realizado y guardado en 'backup.json' con éxito.")
        
    except FileNotFoundError:
        print(f"[{time.strftime('%X')}]  Error: El archivo 'inventario.json' no fue encontrado.")
    except json.JSONDecodeError:
        print(f"[{time.strftime('%X')}] Error: El archivo JSON tiene la estructura rota.")

async def main():
    tarea_monitoreo = asyncio.create_task(monitorear_sistema())
    
    try:
        await asyncio.wait_for(hacer_backup(), timeout=1.0)
    except asyncio.TimeoutError:
        print(f"[{time.strftime('%X')}]  Alerta: El backup falló por lentitud del disco.")
    
    await asyncio.sleep(5)
    
    tarea_monitoreo.cancel()

if __name__ == "__main__":
    asyncio.run(main())