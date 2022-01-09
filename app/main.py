from functools import lru_cache
from fastapi import FastAPI, Depends

from app.config import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()


app = FastAPI(dependencies=[Depends(get_settings)])


@app.get("/")
async def root():
    return {"message": "Hello world"}
