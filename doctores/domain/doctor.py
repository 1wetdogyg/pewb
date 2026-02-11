from pydantic import BaseModel


class Doctor(BaseModel):
    id: str
    nombre: str
    especialidad: str


class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str


class DoctorUpdate(BaseModel):
    nombre: str = None
    especialidad: str = None
