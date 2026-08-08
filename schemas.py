from pydantic import BaseModel, EmailStr
class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True
