from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from src.config.database import Base, engine
from src.controllers.users import UserController

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(UserController().router)


@app.get("/api/health")
def health():
    return {"Health": "OK!"}
