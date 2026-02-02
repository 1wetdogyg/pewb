from usuarios.application.ports.pedido_repository import PedidoRepository
from usuarios.domain.pedido import Pedido

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def consultar_pedido(self, pedido_id: int):
        pedido = self.repository.obtener_por_id(pedido_id)
        return {
            "mensaje": f"Consultando la receta {pedido_id}",
            "equipo_base": pedido.equipo_base
        }

    def crear_pedido(self, pedido: Pedido):
        return self.repository.crear(pedido)
