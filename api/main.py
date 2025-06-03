from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient

from .settings import Settings
from .v1.models import Exam, Institution, Question
from .v1.routes import exams as v1_exams
from .v1.routes import institutions as v1_institutions
from .v1.routes import questions as v1_questions
from .v1.routes import simulado as v1_simulado


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    db = client.delta
    await init_beanie(database=db, document_models=[Institution,
                                                    Exam,
                                                    Question])
    app.mongo_client = client
    yield
    client.close()


app = FastAPI(title='Delta – API de Vestibulares e Concursos'
              , lifespan=lifespan)

app.mount("/static", StaticFiles(directory="assets"), name="static")


app.include_router(
    v1_questions.router, prefix='/api/v1/questions', tags=['v1 - Questions']
)
app.include_router(
    v1_exams.router, prefix='/api/v1/exams', tags=['v1 - Exams']
)
app.include_router(
    v1_simulado.router, prefix='/api/v1/simulados', tags=['v1 - Simulado']
)
app.include_router(
    v1_institutions.router,
    prefix='/api/v1/institutions',
    tags=['v1 - Instituições'],
)
