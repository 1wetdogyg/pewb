from typing import List, Optional
from pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from pacientes.application.ports.paciente_repository import PacienteRepository


class PacienteService:

    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def create_paciente(self, paciente_data: PacienteCreate) -> Paciente:
        if not paciente_data.nombre or not paciente_data.especialidad:
            raise ValueError('nombre and especialidad are required')
        return self.repository.save(paciente_data)

    def get_paciente(self, paciente_id: str) -> Optional[Paciente]:
        return self.repository.find_by_id(paciente_id)

    def get_all_pacientes(self) -> List[Paciente]:
        return self.repository.find_all()

    def update_paciente(self, paciente_id: str, paciente_update: PacienteUpdate) -> Optional[Paciente]:
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        return self.repository.update(paciente_id, paciente_update)

    def delete_paciente(self, paciente_id: str) -> bool:
        return self.repository.delete(paciente_id)
