from fastapi import FastAPI

from routers import memos

from models     import  Base

from connection import engine

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(memos.router)

@app.get("/")
async def root():
    return {"message" : "수훈이의 FastAPI 메모장~!"}
