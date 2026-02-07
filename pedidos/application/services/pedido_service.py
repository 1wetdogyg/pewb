from typing import List, Optional
from domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from application.ports.pedido_repository import PedidoRepository
from infrastructure.adapters.user_client import UserClient


class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository
        self.user_client = UserClient()

    def create_pedido(self, pedido_data: PedidoCreate) -> Pedido:

        # Validar total
        if pedido_data.total <= 0:
            raise ValueError("Total must be greater than 0")

        # Validar que usuario exista
        if not self.user_client.user_exists(pedido_data.user_id):
            raise ValueError("User does not exist")

        return self.repository.save(pedido_data)

    def get_pedido(self, pedido_id: str) -> Optional[Pedido]:
        return self.repository.find_by_id(pedido_id)

    def get_all_pedidos(self) -> List[Pedido]:
        return self.repository.find_all()

    def update_pedido(self, pedido_id: str, pedido_update: PedidoUpdate) -> Optional[Pedido]:
        return self.repository.update(pedido_id, pedido_update)

    def delete_pedido(self, pedido_id: str) -> bool:
        return self.repository.delete(pedido_id)
