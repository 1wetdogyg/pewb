from typing import List, Optional
from uuid import uuid4
from pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from pacientes.application.ports.paciente_repository import PacienteRepository


class PacienteRepositoryImpl(PacienteRepository):

    def __init__(self):
        self.pacientes: List[Paciente] = []

    def save(self, paciente_data: PacienteCreate) -> Paciente:
        new_paciente = Paciente(
            id=str(uuid4()),
            nombre=paciente_data.nombre,
            especialidad=paciente_data.especialidad
        )
        self.pacientes.append(new_paciente)
        return new_paciente

    def find_by_id(self, paciente_id: str) -> Optional[Paciente]:
        for paciente in self.pacientes:
            if paciente.id == paciente_id:
                return paciente
        return None

    def find_all(self) -> List[Paciente]:
        return self.pacientes

    def update(self, paciente_id: str, paciente_update: PacienteUpdate) -> Optional[Paciente]:
        paciente = self.find_by_id(paciente_id)
        if not paciente:
            return None

        if paciente_update.nombre is not None:
            paciente.nombre = paciente_update.nombre

        if paciente_update.especialidad is not None:
            paciente.especialidad = paciente_update.especialidad

        return paciente

    def delete(self, paciente_id: str) -> bool:
        paciente = self.find_by_id(paciente_id)
        if not paciente:
            return False

        self.pacientes.remove(paciente)
        return True
