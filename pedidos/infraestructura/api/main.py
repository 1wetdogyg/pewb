from fastapi import FastAPI
from infraestructura.adapters.pedido_repository_impl import PedidoRepositoryImpl
from application.services.pedido_service import PedidoService

app = FastAPI()

repo = PedidoRepositoryImpl()
service = PedidoService(repo)

@app.post("/pedidos")
def crear_pedido(pedido: dict):
    service.crear_pedido(
        pedido["idpedido"],
        pedido["idusuario"],
        pedido["total"]
    )
    return {"mensaje": "Pedido creado"}

@app.get("/pedidos")
def listar_pedidos():
    return service.listar_pedidos()

@app.get("/pedidos/{idpedido}")
def obtener_pedido(idpedido: int):
    return service.obtener_pedido(idpedido)

@app.put("/pedidos/{idpedido}")
def actualizar_pedido(idpedido: int, pedido: dict):
    service.actualizar_pedido(
        idpedido,
        pedido["idusuario"],
        pedido["total"]
    )
    return {"mensaje": "Pedido actualizado"}

@app.delete("/pedidos/{idpedido}")
def eliminar_pedido(idpedido: int):
    service.eliminar_pedido(idpedido)
    return {"mensaje": "Pedido eliminado"}
