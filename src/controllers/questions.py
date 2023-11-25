from src.models.predictive import Predictive
from src.firebase.connection import get_questions
from src.helpers.keywords import extract_keywords
from src.helpers.context import extract_context


def answer_question(question):
    keywords = extract_keywords(question)
    print(keywords)
    if keywords is False: return {"question":question,"result":"Por favor formule una pregunta adecuada"}
    context = validate_context(keywords)
    print(context)
    if context is "": return {"question":question,"result":"La pregunta no esta disponible, gracias por las nuevas sugerencias"}
    return result_to_question(question,context)

def validate_context(keywords):
    data = get_questions()
    return  extract_context(data,keywords) 

def result_to_question(question,context):
    predictive = Predictive("mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es").get_model()
    results  =  predictive({'question': question,'context':context})
    # Sacamos la diferencia entre start y end, ordenamos en base a la direnrecia mas alta
    best_result  =  max(results, key = lambda x: x["end"] - x["start"])
    print({"question":question,"result":best_result['answer']})
    return {"question":question,"result":best_result['answer']}
