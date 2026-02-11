from fastapi import APIRouter, HTTPException
from typing import List
from pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from pacientes.application.services.paciente_service import PacienteService
from pacientes.infrastructure.adapters.paciente_repository_impl import PacienteRepositoryImpl


router = APIRouter()

repository = PacienteRepositoryImpl()
service = PacienteService(repository)


@router.post('/pacientes', response_model=Paciente)
def create_paciente(paciente: PacienteCreate):
    try:
        return service.create_paciente(paciente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/pacientes/{paciente_id}', response_model=Paciente)
def get_paciente(paciente_id: str):
    paciente = service.get_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail='Paciente not found')
    return paciente


@router.get('/pacientes', response_model=List[Paciente])
def get_all_pacientes():
    return service.get_all_pacientes()


@router.put('/pacientes/{paciente_id}', response_model=Paciente)
def update_paciente(paciente_id: str, paciente_update: PacienteUpdate):
    try:
        updated_paciente = service.update_paciente(paciente_id, paciente_update)
        if not updated_paciente:
            raise HTTPException(status_code=404, detail='Paciente not found')
        return updated_paciente
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete('/pacientes/{paciente_id}')
def delete_paciente(paciente_id: str):
    deleted = service.delete_paciente(paciente_id)
    if not deleted:
        raise HTTPException(status_code=404, detail='Paciente not found')
    return {'message': 'Paciente deleted successfully'}
