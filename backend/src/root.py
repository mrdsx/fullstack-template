from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from constants import ALLOWED_ORIGINS
from router import router as custom_router
from models import BaseResponse


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=custom_router)


@app.get("/", response_model=BaseResponse)
async def read_root() -> BaseResponse:
    return BaseResponse(message="Hello, FastAPI!")
