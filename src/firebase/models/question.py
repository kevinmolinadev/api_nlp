class Question:
    def __init__(self, question, context):
        self.question = question
        self.context = context
    
    @staticmethod
    def from_dict(source):
        return Question(source["question"],source["context"])