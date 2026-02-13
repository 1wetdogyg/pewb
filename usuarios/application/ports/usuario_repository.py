from abc import ABC, abstractmethod
from typing import List
from domain.usuario import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def crear(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Usuario]:
        pass

    @abstractmethod
    def obtener_por_id(self, idusuario: int) -> Usuario:
        pass

    @abstractmethod
    def actualizar(self, idusuario: int, nombre: str, email: str):
        pass

    @abstractmethod
    def eliminar(self, idusuario: int):
        pass
