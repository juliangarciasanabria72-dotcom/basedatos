from pydantic import BaseModel,Field
from typing import  Optional

class productoCreate(BaseModel):
    codigo: str = Field(..., min_length=3, max_length=50, description="Código único del producto", example="PROD001")
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del producto", example="Producto de ejemplo")
    categoria: str
    precio: float = Field(..., gt=0, description="El precio debe ser mayor a 0", example=19.99)
    stock: int = Field(default=0, ge=0, description="El stock no puede ser negativo", example=100)
    compatible_con: Optional[str] = None