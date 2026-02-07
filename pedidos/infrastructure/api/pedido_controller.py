from fastapi import APIRouter, HTTPException
from typing import List

from domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from application.services.pedido_service import PedidoService
from infrastructure.adapters.pedido_repository_impl import PedidoRepositoryImpl


router = APIRouter()

repository = PedidoRepositoryImpl()
service = PedidoService(repository)


@router.post("/pedidos", response_model=Pedido)
def create_pedido(pedido: PedidoCreate):
    try:
        return service.create_pedido(pedido)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/pedidos", response_model=List[Pedido])
def get_all_pedidos():
    return service.get_all_pedidos()


@router.get("/pedidos/{pedido_id}", response_model=Pedido)
def get_pedido(pedido_id: str):
    pedido = service.get_pedido(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return pedido


@router.put("/pedidos/{pedido_id}", response_model=Pedido)
def update_pedido(pedido_id: str, pedido_update: PedidoUpdate):
    updated = service.update_pedido(pedido_id, pedido_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return updated


@router.delete("/pedidos/{pedido_id}")
def delete_pedido(pedido_id: str):
    deleted = service.delete_pedido(pedido_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return {"message": "Pedido deleted successfully"}
