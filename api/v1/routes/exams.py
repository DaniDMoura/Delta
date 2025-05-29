from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def gerar():
    return {'ola': 'mundo'}
