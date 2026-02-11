from typing import List, Optional
from doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from doctores.application.ports.doctor_repository import DoctorRepository


class DoctorService:

    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def create_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        if not doctor_data.nombre or not doctor_data.especialidad:
            raise ValueError('nombre and especialidad are required')
        return self.repository.save(doctor_data)

    def get_doctor(self, doctor_id: str) -> Optional[Doctor]:
        return self.repository.find_by_id(doctor_id)

    def get_all_doctors(self) -> List[Doctor]:
        return self.repository.find_all()

    def update_doctor(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None
        return self.repository.update(doctor_id, doctor_update)

    def delete_doctor(self, doctor_id: str) -> bool:
        return self.repository.delete(doctor_id)
