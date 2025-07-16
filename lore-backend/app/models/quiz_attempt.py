# models/quiz_attempt.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    question_id = Column(String)
    chapter = Column(String)
    correct = Column(Boolean)
