from fastapi import APIRouter
from src.models.question import Question

from src.firebase.connection import get_questions
from src.controllers.questions import answer_question


questions = APIRouter()
@questions.get("/questions")
async def get_all_questions():
    return get_questions()

@questions.post("/questions")
async def get_result(model: Question):
    return answer_question(model.question)
