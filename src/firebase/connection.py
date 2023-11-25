import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from src.firebase.firebase_config import credential
from src.firebase.models.question import Question

cred = credentials.Certificate(credential)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

#QUESTION
def get_questions():
    questions=[]
    questions_data=db.collection('questions').stream()
    for item in questions_data:
        question = Question.from_dict(item.to_dict())
        questions.append(question)
    return questions

