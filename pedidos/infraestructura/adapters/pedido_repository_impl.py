from application.ports.pedido_repository import PedidoRepository
from domain.pedido import Pedido

class PedidoRepositoryImpl(PedidoRepository):

    def __init__(self):
        self.pedidos = []

    def crear(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def obtener_todos(self):
        return self.pedidos

    def obtener_por_id(self, idpedido: int):
        for p in self.pedidos:
            if p.idpedido == idpedido:
                return p
        return None

    def actualizar(self, idpedido: int, idusuario: int, total: float):
        pedido = self.obtener_por_id(idpedido)
        if pedido:
            pedido.idusuario = idusuario
            pedido.total = total

    def eliminar(self, idpedido: int):
        self.pedidos = [p for p in self.pedidos if p.idpedido != idpedido]
