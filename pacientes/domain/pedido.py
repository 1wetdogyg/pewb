from pydantic import BaseModel
from typing import List

class Pedido(BaseModel):
    id: int
    equipo_base: List[str]
