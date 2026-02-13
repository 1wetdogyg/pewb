from application.ports.pedido_repository import PedidoRepository
from domain.pedido import Pedido

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def crear_pedido(self, idpedido, idusuario, total):
        pedido = Pedido(idpedido, idusuario, total)
        self.repository.crear(pedido)

    def listar_pedidos(self):
        return self.repository.obtener_todos()

    def obtener_pedido(self, idpedido):
        return self.repository.obtener_por_id(idpedido)

    def actualizar_pedido(self, idpedido, idusuario, total):
        self.repository.actualizar(idpedido, idusuario, total)

    def eliminar_pedido(self, idpedido):
        self.repository.eliminar(idpedido)
