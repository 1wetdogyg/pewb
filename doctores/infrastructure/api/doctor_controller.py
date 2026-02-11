from fastapi import APIRouter, HTTPException
from typing import List
from doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from doctores.application.services.doctor_service import DoctorService
from doctores.infrastructure.adapters.doctor_repository_impl import DoctorRepositoryImpl


router = APIRouter()

repository = DoctorRepositoryImpl()
service = DoctorService(repository)


@router.post('/doctores', response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    try:
        return service.create_doctor(doctor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/doctores/{doctor_id}', response_model=Doctor)
def get_doctor(doctor_id: str):
    doctor = service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail='Doctor not found')
    return doctor


@router.get('/doctores', response_model=List[Doctor])
def get_all_doctors():
    return service.get_all_doctors()


@router.put('/doctores/{doctor_id}', response_model=Doctor)
def update_doctor(doctor_id: str, doctor_update: DoctorUpdate):
    try:
        updated_doctor = service.update_doctor(doctor_id, doctor_update)
        if not updated_doctor:
            raise HTTPException(status_code=404, detail='Doctor not found')
        return updated_doctor
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete('/doctores/{doctor_id}')
def delete_doctor(doctor_id: str):
    deleted = service.delete_doctor(doctor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail='Doctor not found')
    return {'message': 'Doctor deleted successfully'}
