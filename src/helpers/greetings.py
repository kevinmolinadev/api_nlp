import re

def is_greetings(question):
    saludos = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches"]
    return any(re.search(rf'\b{re.escape(saludo)}\b', question, re.IGNORECASE) for saludo in saludos)
