from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import StudentResponse
from student_service import search_students

router = APIRouter()


@router.get("/students/search", response_model=list[StudentResponse])
def search(
    keyword: Optional[str] = None,
    min_age: Optional[int] = Query(None, ge=0),
    max_age: Optional[int] = Query(None, ge=0),
    is_active: Optional[bool] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    return search_students(
        db, keyword, min_age, max_age,
        is_active, page, page_size
    )
