from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def list_questions(): ...


@router.get('/')
def list_question(): ...
