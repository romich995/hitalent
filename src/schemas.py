import datetime
import uuid

from pydantic import BaseModel, Field, ConfigDict


class QuestionPost(BaseModel):
    text: str = Field(min_length=10)

    model_config = ConfigDict(from_attributes=True)


class QuestionGet(QuestionPost):
    id: int
    created_at: datetime.datetime


class AnswerPost(BaseModel):
    user_id: uuid.UUID
    text: str

    model_config = ConfigDict(from_attributes=True)


class AnswerGet(AnswerPost):
    id: int
    question_id: int
    created_at: datetime.datetime



class QuestionWithAnswers(QuestionGet):
    answers: list[AnswerGet]


