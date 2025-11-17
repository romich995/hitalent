import datetime
import uuid

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Uuid


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "questions"
    id:  Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow, index=True)

    answers: Mapped[list["Answer"]] = relationship(back_populates="question", order_by="Answer.created_at", cascade="all, delete-orphan")


class Answer(Base):
    __tablename__ = "answers"
    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    text: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow, index=True)


    question: Mapped["Question"] = relationship(back_populates="answers",)
