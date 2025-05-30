from typing import Annotated

from fastapi import APIRouter, Query

router = APIRouter()


@router.get('/')
def list_institutions(
    institutions: Annotated[list[str] | None, Query()] = None,
    years: Annotated[list[int] | None, Query()] = None,
):
    ...


@router.get('/{question_id}')
def list_institution(question_id: int):
    ...
