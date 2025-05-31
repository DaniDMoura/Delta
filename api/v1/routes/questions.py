from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from ..models import Question
from ..schemas import ListQuestion

router = APIRouter()


@router.get('/', response_model=ListQuestion,
            status_code=HTTPStatus.OK)
async def list_question(
    institution: Annotated[list[str] | None, Query()] = None,
    year: Annotated[list[int] | None, Query()] = None,
    index: Annotated[list[int] | None, Query()] = None
                  ):

    filters = {}

    if institution:
        filters["institution"] = {"$in": institution}
    if year:
        filters["year"] = {"$in": year}
    if index:
        filters["index"] = {"$in": index}

    question_data = await Question.find(filters).to_list()
    if not question_data:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="No questions available"
        )

    return {"Questions": question_data}
