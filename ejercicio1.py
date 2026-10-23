from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import json
import os

app = FastAPI(
    title="Taller Mecánico - Sistema de Órdenes",
    description="API para el control y recepción de motocicletas",
    version="1.0.0"
)

ARCHIVO_JSON = "taller.json"

async def leer_taller():
    if not os.path.exists(ARCHIVO_JSON):
        return []
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

async def guardar_taller(datos):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

# --- Esquemas Pydantic ---
class OrdenCreate(BaseModel):
    placa: str = Field(..., max_length=6, description="Placa de la motocicleta (máximo 6 caracteres)")
    modelo: str = Field(..., description="Modelo de la moto")
    falla_reportada: str = Field(..., description="Descripción de la falla")

class OrdenUpdate(BaseModel):
    nuevo_estado: str = Field(..., description="Nuevo estado de la orden")
    costo_reparacion: float = Field(..., description="Costo correspondiente a la reparación")

@app.post("/ordenes", status_code=201)
async def crear_orden(orden: OrdenCreate):
    datos = await leer_taller()
    
    for item in datos:
        if item["placa"].upper() == orden.placa.upper():
            if item["estado"] != "Entregada":
                raise HTTPException(
                    status_code=400, 
                    detail="La moto ya se encuentra en el taller"
                )
                
    nueva_orden = {
        "placa": orden.placa.upper(),
        "modelo": orden.modelo,
        "falla_reportada": orden.falla_reportada,
        "estado": "En diagnóstico",
        "costo_reparacion": 0
    }
    
    datos.append(nueva_orden)
    await guardar_taller(datos)
    
    return {
        "mensaje": "Orden de ingreso creada exitosamente", 
        "orden": nueva_orden
    }

@app.get("/ordenes")
async def consultar_ordenes():
    datos = await leer_taller()
    return {
        "cantidad": len(datos), 
        "ordenes": datos
    }

@app.put("/ordenes/{placa}")
async def actualizar_orden(placa: str, actualizacion: OrdenUpdate):
    datos = await leer_taller()
    
    orden_encontrada = None
    for item in datos:
        if item["placa"].upper() == placa.upper():
            orden_encontrada = item
            break
            
    if not orden_encontrada:
        raise HTTPException(
            status_code=404, 
            detail="La orden con la placa especificada no existe"
        )
        
    if actualizacion.nuevo_estado.lower() == "reparada" and actualizacion.costo_reparacion <= 0:
        raise HTTPException(
            status_code=400, 
            detail="No se puede marcar como reparada sin asignar un costo de reparación"
        )
        
    orden_encontrada["estado"] = actualizacion.nuevo_estado
    orden_encontrada["costo_reparacion"] = actualizacion.costo_reparacion
    
    await guardar_taller(datos)
    
    return {
        "mensaje": "Orden actualizada exitosamente", 
        "orden": orden_encontrada
    }