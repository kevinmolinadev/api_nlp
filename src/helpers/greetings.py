import re

def get_greetings(question):
    words = question.split(" ")
    if(len(words)>4): return [False,None]
    saludos = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches"]
    for saludo in saludos:
        if re.search(rf'\b{re.escape(saludo)}\b', question, re.IGNORECASE):
            return [True, saludo]
    return [False, None]
