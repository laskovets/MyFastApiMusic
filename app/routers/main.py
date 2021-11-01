from fastapi.routing import APIRouter


router = APIRouter()


@router.get('/', status_code=200)
async def root() -> dict:
    return {'response': 'hello world'}
