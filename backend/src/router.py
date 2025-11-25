from fastapi.routing import APIRouter

from models import BaseResponse


router = APIRouter()


@router.get("/endpoint", response_model=BaseResponse)
async def custom_endpoint() -> BaseResponse:
    return BaseResponse(message="Hello from endpoint!")
