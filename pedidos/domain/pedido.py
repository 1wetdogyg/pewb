from pydantic import BaseModel
from typing import Optional


class Pedido(BaseModel):
    id: str
    user_id: str
    descripcion: str
    total: float


class PedidoCreate(BaseModel):
    user_id: str
    descripcion: str
    total: float


class PedidoUpdate(BaseModel):
    descripcion: Optional[str] = None
    total: Optional[float] = None
