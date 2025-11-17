from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db import get_db_session
from models import Answer
from schemas import AnswerPost, AnswerGet


answer_api_router = APIRouter()

@answer_api_router.post("/questions/{id}/answers/", status_code=201, response_model=AnswerGet)
async def append_answer_to_question(id: int,
                                    answer: AnswerPost,
                              async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    try:
        answer = Answer(question_id=id, user_id=answer.user_id, text=answer.text)
        async_session.add(answer)
        await async_session.commit()
    except Exception as err:
        print(err)
        raise HTTPException(404, "Question not found")

    return answer

@answer_api_router.get("/answers/{id}", response_model=AnswerGet)
async def get_answer_by_id(id: int,
                              async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    answer = await async_session.get(Answer, id)

    if not answer:
        raise HTTPException(404, "Answer not found")

    return answer

@answer_api_router.delete("/answer/{id}", status_code=204)
async def delete_answer_by_id(id: int,
                              async_session: Annotated[AsyncSession, Depends(get_db_session)]):
    answer = await async_session.get(Answer, id)

    if not answer:
        return

    await async_session.delete(answer)
    await async_session.commit()

