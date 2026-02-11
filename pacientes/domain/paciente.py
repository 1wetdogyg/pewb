from pydantic import BaseModel


class Paciente(BaseModel):
    id: str
    nombre: str
    especialidad: str


class PacienteCreate(BaseModel):
    nombre: str
    especialidad: str


class PacienteUpdate(BaseModel):
    nombre: str = None
    especialidad: str = None


User = Paciente
UserCreate = PacienteCreate
UserUpdate = PacienteUpdate
