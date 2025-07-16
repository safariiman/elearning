#routes/personalized_quiz.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.utils.quiz_performance import get_user_performance_by_chapter

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/personalized-quiz/{user_id}")
def get_personalized_quiz(user_id: str, db: Session = Depends(get_db)):
    chapter_stats = get_user_performance_by_chapter(db, user_id)
    if not chapter_stats:
        raise HTTPException(status_code=404, detail="No quiz data for user")

    weakest_chapter = max(chapter_stats, key=lambda ch: chapter_stats[ch]["incorrect"])
    # Optionally, attach the stats for use by the next module
    return {
        "weakest_chapter": weakest_chapter,
        "per_chapter_stats": chapter_stats[weakest_chapter],
    }
