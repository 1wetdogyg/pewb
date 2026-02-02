from fastapi import APIRouter
from usuarios.domain.pedido import Pedido
from usuarios.application.services.pedido_service import PedidoService
from usuarios.infrastructure.adapters.pedido_mem_adapter import PedidoMemAdapter

router = APIRouter()

service = PedidoService(PedidoMemAdapter())

@router.get("/pedidos/{pedido_id}")
def get_pedido(pedido_id: int):
    return service.consultar_pedido(pedido_id)

@router.post("/pedidos")
def post_pedido(pedido: Pedido):
    return service.crear_pedido(pedido)
