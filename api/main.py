from fastapi import FastAPI

from .v1.routes import exams as v1_exams
from .v1.routes import institutions as v1_institutions
from .v1.routes import questions as v1_questions
from .v1.routes import simulado as v1_simulado

app = FastAPI(title='Project Delta – API de Vestibulares e Concursos')


app.include_router(v1_questions.router, prefix="/api/v1/questions"
                   , tags=["v1 - Questions"])
app.include_router(v1_exams.router, prefix="/api/v1/exams"
                   , tags=["v1 - Exams"])
app.include_router(v1_simulado.router, prefix="/api/v1/simulados"
                   , tags=["v1 - Simulado"])
app.include_router(v1_institutions.router, prefix="/api/v1/institutions"
                   , tags=["v1 - Instituições"])
