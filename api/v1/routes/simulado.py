import random
from http import HTTPStatus
from typing import Annotated, Optional

from fastapi import APIRouter, HTTPException, Query

from ..models import Question
from ..schemas import ListQuestion

router = APIRouter()


@router.post('/', response_model=ListQuestion, status_code=HTTPStatus.OK)
async def generate_simulado(
    number_of_questions: int =
    Query(..., gt=0, description="Número de questões a gerar"),
    institution: Annotated[list[str] | None, Query()] = None,
    year: Optional[int] = Query(None, description="Ano da prova"),
):
    filters = {}

    if institution:
        filters["institution"] = {"$in": institution}
    if year:
        filters["year"] = year

    question_data = await Question.find(filters).to_list()
    if len(question_data) < number_of_questions:
        raise HTTPException(
        status_code=HTTPStatus.BAD_REQUEST,
        detail=f"Not enough available questions. Found: {len(question_data)}"
        )

    selected = random.sample(question_data, number_of_questions)

    return ListQuestion(Questions=selected)
