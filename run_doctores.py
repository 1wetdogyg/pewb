from fastapi import FastAPI
from uvicorn import run
from doctores.infrastructure.api.doctor_controller import router as doctor_router

app = FastAPI(title='Doctores API', version='1.0.0')
app.include_router(doctor_router)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8001)
