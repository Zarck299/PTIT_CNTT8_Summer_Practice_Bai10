from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Student


def search_students(
    db: Session,
    keyword,
    min_age,
    max_age,
    is_active,
    page,
    page_size
):
    try:
        if min_age is not None and max_age is not None:
            if min_age > max_age:
                raise HTTPException(
                    status_code=400,
                    detail="min_age không được lớn hơn max_age"
                )

        query = db.query(Student)

        if keyword:
            query = query.filter(
                (Student.name.ilike(f"%{keyword}%")) |
                (Student.email.ilike(f"%{keyword}%"))
            )

        if min_age is not None:
            query = query.filter(Student.age >= min_age)

        if max_age is not None:
            query = query.filter(Student.age <= max_age)

        if is_active is not None:
            query = query.filter(Student.is_active == is_active)

        offset = (page - 1) * page_size

        return query.offset(offset).limit(page_size).all()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
