from typing import List, Optional
from uuid import uuid4
from domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from application.ports.pedido_repository import PedidoRepository


class PedidoRepositoryImpl(PedidoRepository):

    def __init__(self):
        self.pedidos: List[Pedido] = []

    def save(self, pedido_data: PedidoCreate) -> Pedido:
        new_pedido = Pedido(
            id=str(uuid4()),
            user_id=pedido_data.user_id,
            descripcion=pedido_data.descripcion,
            total=pedido_data.total
        )
        self.pedidos.append(new_pedido)
        return new_pedido


    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        for pedido in self.pedidos:
            if pedido.id == pedido_id:
                return pedido
        return None

    def find_all(self) -> List[Pedido]:
        return self.pedidos

    def update(self, pedido_id: str, pedido_update: PedidoUpdate) -> Optional[Pedido]:
        pedido = self.find_by_id(pedido_id)
        if not pedido:
            return None

        if pedido_update.descripcion is not None:
            pedido.descripcion = pedido_update.descripcion

        if pedido_update.total is not None:
            pedido.total = pedido_update.total

        return pedido

    def delete(self, pedido_id: str) -> bool:
        pedido = self.find_by_id(pedido_id)
        if not pedido:
            return False

        self.pedidos.remove(pedido)
        return True
