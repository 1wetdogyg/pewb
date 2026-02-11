from typing import List, Optional
from uuid import uuid4
from doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from doctores.application.ports.doctor_repository import DoctorRepository


class DoctorRepositoryImpl(DoctorRepository):

    def __init__(self):
        self.doctors: List[Doctor] = []

    def save(self, doctor_data: DoctorCreate) -> Doctor:
        new_doctor = Doctor(
            id=str(uuid4()),
            nombre=doctor_data.nombre,
            especialidad=doctor_data.especialidad
        )
        self.doctors.append(new_doctor)
        return new_doctor

    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def find_all(self) -> List[Doctor]:
        return self.doctors

    def update(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        doctor = self.find_by_id(doctor_id)
        if not doctor:
            return None

        if doctor_update.nombre is not None:
            doctor.nombre = doctor_update.nombre

        if doctor_update.especialidad is not None:
            doctor.especialidad = doctor_update.especialidad

        return doctor

    def delete(self, doctor_id: str) -> bool:
        doctor = self.find_by_id(doctor_id)
        if not doctor:
            return False

        self.doctors.remove(doctor)
        return True
