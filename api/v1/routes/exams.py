from typing import Annotated

from fastapi import APIRouter, Query

router = APIRouter()


@router.get('/')
def list_exam(
    institutions: Annotated[list[str] | None, Query()] = None,
    years: Annotated[list[int] | None, Query()] = None,
): ...
