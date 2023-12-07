from src.models.predictive import Predictive
from src.firebase.connection import get_questions
from src.helpers.keywords import extract_keywords
from src.helpers.context import extract_context
from src.helpers.greetings import is_greetings


def answer_question(question):
    if is_greetings(question) is True: return {"question":question,"result":f"¡{question}! Soy A.V.U, tu Asistente Virtual Univalle. Estoy aquí para ayudarte en lo que necesites. ¿En qué puedo asistirte hoy?"}
    keywords = extract_keywords(question)
    if keywords is False: return {"question":question,"result":"😕 ¡Ups! No entendí bien la pregunta. ¿Podrías reformularla, por favor?"}
    context = validate_context(keywords)
    if context == "": return {"question":question,"result":"🌟 ¡Gracias por tu pregunta! Sin embargo, no tengo información sobre ese tema. ¿Puedes preguntar algo diferente?"}
    return result_to_question(question,context)

def validate_context(keywords):
    data = get_questions()
    return  extract_context(data,keywords) 

def result_to_question(question,context):
    predictive = Predictive("mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es").get_model()
    results  =  predictive({'question': question,'context':context})
    # Sacamos la diferencia entre start y end, ordenamos en base a la direnrecia mas alta
    best_result  =  max(results, key = lambda x: x["end"] - x["start"])
    return {"question":question,"result":best_result['answer']}
