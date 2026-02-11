from pydantic import BaseModel
from typing import Optional

class producto(BaseModel):
    id: str
    nombre: str
    precio:float
    stock: int

class ProductosCreate(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoUpdate(BaseModel):
    nombre: Optional[str]=None
    precio: Optional[float]=None
    stock: Optional[int]=None