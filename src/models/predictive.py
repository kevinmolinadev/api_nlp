from dotenv import load_dotenv
from openai import OpenAI
from datetime import date

class Predictive:
    def __init__(self,question, contexts):
        self.question=question
        self.contexts=contexts
        self.messages=[]
    
    def _build_context(self):
        header_message={"role": 
                        "system", "content": f"Eres un asistente de la universidad y tienes acceso a información sobre la universidad. Utiliza ese conocimiento para responder a 
                        las preguntas de manera precisa. Actualmente estamos en el año {date.today().year}"}
        body_messages =  "\n".join(self.contexts)
        body_message = {"role": "assistant", "content": body_messages}
        question_message = {"role": "user", "content": self.question}
        self.messages = [header_message] + [body_message] + [question_message]
        return self.messages

    def get_answer_question(self):
        load_dotenv()
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=self._build_context(),
            temperature=0
        )
        return response.choices[0].message.content