from fastapi import FastAPI
from infrastructure.api.pedido_controller import router as pedido_router

app = FastAPI()

app.include_router(pedido_router)
