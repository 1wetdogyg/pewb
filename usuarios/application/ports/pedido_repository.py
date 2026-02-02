from abc import ABC, abstractmethod
from usuarios.domain.pedido import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def obtener_por_id(self, pedido_id: int) -> Pedido:
        pass

    @abstractmethod
    def crear(self, pedido: Pedido) -> Pedido:
        pass
