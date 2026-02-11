from usuarios.application.ports.pedido_repository import PedidoRepository
from usuarios.domain.pedido import Pedido

class PedidoMemAdapter(PedidoRepository):

    def __init__(self):
        self.data = {
            100: Pedido(
                id=100,
                equipo_base=[
                    "Sartén de teflón",
                    "Cuchillo de chef",
                    "Espátula"
                ]
            )
        }

    def obtener_por_id(self, pedido_id: int) -> Pedido:
        return self.data.get(pedido_id, Pedido(id=pedido_id, equipo_base=[]))

    def crear(self, pedido: Pedido) -> Pedido:
        self.data[pedido.id] = pedido
        return pedido
