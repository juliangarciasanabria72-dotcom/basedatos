import asyncio
import random
import time

async def descargar_factura(numero_factura):
    tiempo_espera = random.randint(1, 3)
    print(f"[{time.strftime('%X')}] Iniciando descarga de factura #{numero_factura} (Tardará {tiempo_espera}s)")
    
    await asyncio.sleep(tiempo_espera)
    
    print(f"[{time.strftime('%X')}] Factura #{numero_factura} descargada exitosamente")
    return f"Factura #{numero_factura}"

async def main():
    print("INICIO DEL PROGRAMA ASÍNCRONO ")
    inicio = time.time()
    
    tareas = [
        descargar_factura(1),
        descargar_factura(2),
        descargar_factura(3),
        descargar_factura(4),
        descargar_factura(5)
    ]
    
    resultados = await asyncio.gather(*tareas)
    
    fin = time.time()
    print("--- FIN DEL PROGRAMA ---")
    print(f"Tiempo total: {fin - inicio:.2f} segundos")

asyncio.run(main()) 