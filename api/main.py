from fastapi import FastAPI

from .v1.routes import exams as v1_exams
from .v1.routes import questions as v1_questions
from .v2.routes import exams as v2_exams
from .v2.routes import questions as v2_questions

app = FastAPI(title='Project Delta')

app.include_router(
    v1_questions.router, prefix='/api/v1/questions', tags=['v1 - Questions']
)
app.include_router(
    v1_exams.router, prefix='/api/v1/exams', tags=['v1 - Exams']
)
app.include_router(
    v2_questions.router, prefix='/api/v2/questions', tags=['v2 - Questions']
)
app.include_router(
    v2_exams.router, prefix='/api/v2/exams', tags=['v2 - Exams']
)
