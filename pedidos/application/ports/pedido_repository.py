from abc import ABC, abstractmethod
from typing import List
from domain.pedido import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def crear(self, pedido: Pedido):
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Pedido]:
        pass

    @abstractmethod
    def obtener_por_id(self, idpedido: int) -> Pedido:
        pass

    @abstractmethod
    def actualizar(self, idpedido: int, idusuario: int, total: float):
        pass

    @abstractmethod
    def eliminar(self, idpedido: int):
        pass
