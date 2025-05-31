from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from ..models import Institution
from ..schemas import ListInstitutions

router = APIRouter()


@router.get('/',
            response_model=ListInstitutions,
            status_code=HTTPStatus.OK)
async def list_institution(
    institutions: Annotated[list[str] | None, Query()] = None):
    filters = {}

    if institutions:
        filters["name"] = {"$in": institutions}

    institutions_data = await Institution.find(filters).to_list()
    if not institutions_data:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="No institutions available"
        )

    return {"Institutions": institutions_data}
