import asyncio

async def cobrar_tarjeta(monto):
    print("Conectando con mercadopago...")
    await asyncio.sleep(10)
    return "Pago aprobado"

async def procesar_compra():
    try:
        # Se le va a dar el máximo de 3 seg
        resultado = await asyncio.wait_for(cobrar_tarjeta(150000), timeout=3.1)
        print(f"Exito:{resultado}")
    except asyncio.TimeoutError:
        print("Error:MercadoPago tardo demasiado. Transaccion cancelada.")
        asyncio.run(procesar_compra())