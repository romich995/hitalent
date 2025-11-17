from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db import get_db_session
from models import Question
from schemas import QuestionGet, QuestionPost, QuestionWithAnswers

question_api_router = APIRouter()

@question_api_router.get("/questions/", response_model=list[QuestionGet])
async def get_all_questions(async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    questions_stmt = select(Question).order_by(Question.created_at.desc())
    questions = (await async_session.execute(questions_stmt)).scalars()
    return questions

@question_api_router.post("/questions/", response_model=QuestionGet, status_code=201)
async def create_question(question: QuestionPost,
        async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    question = Question(text=question.text)
    async_session.add(question)
    await async_session.commit()

    return question

@question_api_router.get("/questions/{id}", response_model=QuestionWithAnswers)
async def get_question_with_answers(id: int,
        async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    question_stmt = select(Question).where(Question.id == id).options(selectinload(Question.answers))

    question = (await async_session.execute(question_stmt)).scalar_one_or_none()

    if not question:
        raise HTTPException(404, "Question not found")

    return question

@question_api_router.delete("/questions/{id}", status_code=204)
async def delete_question_with_answers(id: int,
        async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    question_stmt = select(Question).where(Question.id == id).options(selectinload(Question.answers))
    question = (await async_session.execute(question_stmt)).scalar_one_or_none()

    if not question:
        raise HTTPException(404, "Question not found")

    await async_session.delete(question)
    await async_session.commit()

