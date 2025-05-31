from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from ..models import Exam
from ..schemas import ListExam

router = APIRouter()


@router.get('/', response_model=ListExam, status_code=HTTPStatus.OK)
async def list_exam(
    institution: Annotated[list[str] | None, Query()] = None,
    years: Annotated[list[int] | None, Query()] = None,
):
    filters = {}

    if institution:
        filters["institution"] = {"$in": institution}
    if years:
        filters["year"] = {"$in": years}

    exams_data = await Exam.find(filters).to_list()
    if not exams_data:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="No exams available"
        )

    return {"Exams": exams_data}
