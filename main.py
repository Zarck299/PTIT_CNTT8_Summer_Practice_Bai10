from fastapi import FastAPI
from student_router import router

app = FastAPI()

app.include_router(router)
