from application.ports.usuario_repository import UsuarioRepository
from domain.usuario import Usuario

class UsuarioRepositoryImpl(UsuarioRepository):

    def __init__(self):
        self.usuarios = []

    def crear(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def obtener_todos(self):
        return self.usuarios

    def obtener_por_id(self, idusuario: int):
        for u in self.usuarios:
            if u.idusuario == idusuario:
                return u
        return None

    def actualizar(self, idusuario: int, nombre: str, email: str):
        usuario = self.obtener_por_id(idusuario)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email

    def eliminar(self, idusuario: int):
        self.usuarios = [u for u in self.usuarios if u.idusuario != idusuario]
