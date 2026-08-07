import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db.create_all()

    yield

    # Shutdown
    await db.close()

app = FastAPI(lifespan=lifespan)

def start():
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)