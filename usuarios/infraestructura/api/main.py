from fastapi import FastAPI
from pydantic import BaseModel
from infraestructura.adapters.usuario_repository_impl import UsuarioRepositoryImpl
from application.services.usuario_service import UsuarioService

app = FastAPI()

repo = UsuarioRepositoryImpl()
service = UsuarioService(repo)

# Modelo de entrada
class UsuarioRequest(BaseModel):
    idusuario: int
    nombre: str
    email: str

@app.post("/usuarios")
def crear_usuario(usuario: UsuarioRequest):
    service.crear_usuario(
        usuario.idusuario,
        usuario.nombre,
        usuario.email
    )
    return {"mensaje": "Usuario creado"}

@app.get("/usuarios")
def listar_usuarios():
    return service.listar_usuarios()

@app.get("/usuarios/{idusuario}")
def obtener_usuario(idusuario: int):
    return service.obtener_usuario(idusuario)

@app.put("/usuarios/{idusuario}")
def actualizar_usuario(idusuario: int, usuario: UsuarioRequest):
    service.actualizar_usuario(
        idusuario,
        usuario.nombre,
        usuario.email
    )
    return {"mensaje": "Usuario actualizado"}

@app.delete("/usuarios/{idusuario}")
def eliminar_usuario(idusuario: int):
    service.eliminar_usuario(idusuario)
    return {"mensaje": "Usuario eliminado"}
