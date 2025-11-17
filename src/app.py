from fastapi import FastAPI, Depends, HTTPException

from question_api import question_api_router
from answer_api import answer_api_router

app = FastAPI()

app.include_router(question_api_router)

app.include_router(answer_api_router)

