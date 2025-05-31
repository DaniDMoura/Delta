from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.post('/')
def generate_simulado(
    number_of_questions: int, institution: Optional[str], year: Optional[str]
): ...
