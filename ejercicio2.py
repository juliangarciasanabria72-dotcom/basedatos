from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from schemas import OrdenCreate, OrdenPatch, OrdenUpdate
from database import leer_base_datos, guardar_base_datos

router = APIRouter(prefix="/ordenes", tags=["Gestionar ordenes"])

@router.get("/")
async def obtener_ordenes(
    estado: Optional[str] = None,
    modelo: Optional[str] = None,
    costo_minimo: Optional[float] = None
):
    datos = await leer_base_datos()
    datos_filtrados = datos

    # Filtro acumulativo por estado
    if estado:
        datos_filtrados = [
            orden for orden in datos_filtrados 
            if orden.get("estado", "").lower() == estado.lower()
        ]
    
    # Filtro acumulativo por modelo
    if modelo:
        datos_filtrados = [
            orden for orden in datos_filtrados 
            if modelo.lower() in orden.get("modelo", "").lower()
        ]

    # Filtro acumulativo por costo mínimo
    if costo_minimo is not None:
        datos_filtrados = [
            orden for orden in datos_filtrados 
            if orden.get("costo_reparacion", 0.0) >= costo_minimo
        ]
    
    return {
        "total_ordenes": len(datos_filtrados),
        "ordenes": datos_filtrados
    }

