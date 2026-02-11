from fastapi import FastAPI
from uvicorn import run
from pacientes.infrastructure.api.paciente_controller import router as paciente_router

app = FastAPI(title='Pacientes API', version='1.0.0')
app.include_router(paciente_router)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8002)
