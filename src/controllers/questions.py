import re
from src.models.predictive import Predictive
from src.firebase.connection import get_questions
from src.helpers.keywords import extract_keywords
from src.helpers.context import extract_context
from src.helpers.greetings import is_greetings


def answer_question(question):
    thanks_pattern = re.compile(r'\b(gracias|gracias\s+por\s+tu\s+ayuda|hasta\s+luego)\b', re.IGNORECASE)
    if re.search(thanks_pattern, question): return {"question": question,"result": "¡De nada! Es un placer ayudarte. 😊 ¡Hasta luego!"}
    greetings_pattern = re.compile(r'\b(hola|buenos\s+dias|buenas\s+tardes|buenas\s+noches)\b', re.IGNORECASE)
    if re.search(greetings_pattern, question): return {"question":question,"result":f"¡{question}! Soy A.V.U, tu Asistente Virtual Univalle. Estoy aquí para ayudarte en lo que necesites. ¿En qué puedo asistirte hoy?"}
    keywords = extract_keywords(question)
    print(keywords)
    if keywords is False: return {"question":question,"result":"😕 ¡Ups! No entendí bien la pregunta. ¿Podrías reformularla, por favor?"}
    context = validate_context(keywords)
    if context == []: return {"question":question,"result":"🌟 ¡Gracias por tu pregunta! Sin embargo, no tengo información sobre ese tema. ¿Puedes preguntar algo diferente?"}
    return result_to_question(question,context)

def validate_context(keywords):
    data = get_questions()
    return  extract_context(data,keywords) 

def result_to_question(question,contexts):
    predictive= Predictive(question,contexts)
    result= predictive.get_answer_question()
    return {"question":question,"result":result}