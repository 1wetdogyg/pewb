from application.ports.usuario_repository import UsuarioRepository
from domain.usuario import Usuario

class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def crear_usuario(self, idusuario, nombre, email):
        usuario = Usuario(idusuario, nombre, email)
        self.repository.crear(usuario)

    def listar_usuarios(self):
        return self.repository.obtener_todos()

    def obtener_usuario(self, idusuario):
        return self.repository.obtener_por_id(idusuario)

    def actualizar_usuario(self, idusuario, nombre, email):
        self.repository.actualizar(idusuario, nombre, email)

    def eliminar_usuario(self, idusuario):
        self.repository.eliminar(idusuario)
