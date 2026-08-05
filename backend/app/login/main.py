import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get('/')
async def home():
    return 'Welcome Home'

app.include_router(router)