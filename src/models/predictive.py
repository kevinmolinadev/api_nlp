from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
class Predictive:
    def __init__(self,model):
        self._the_model = model
        self._tokenizer = AutoTokenizer.from_pretrained(self._the_model, do_lower_case=False,use_fast=True)
        self._model = AutoModelForQuestionAnswering.from_pretrained(self._the_model)
        self._nlp = pipeline('question-answering', max_seq_len=512, model=self._model, tokenizer=self._tokenizer,top_k=10, max_answer_len=120)
   
    def get_model(self):
        return self._nlp