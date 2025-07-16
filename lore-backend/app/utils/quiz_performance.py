# utils/quiz_performance.py
from sqlalchemy.orm import Session
from app.models.quiz_attempt import QuizAttempt

def get_user_performance_by_chapter(db: Session, user_id: str):
    records = db.query(QuizAttempt).filter(QuizAttempt.user_id == user_id).all()
    chapter_stats = {}
    for r in records:
        ch = r.chapter
        if ch not in chapter_stats:
            chapter_stats[ch] = {"correct": 0, "incorrect": 0}
        if r.correct:
            chapter_stats[ch]["correct"] += 1
        else:
            chapter_stats[ch]["incorrect"] += 1
    return chapter_stats
