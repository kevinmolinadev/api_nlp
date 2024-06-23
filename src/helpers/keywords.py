import re

def extract_keywords(text):
    words = re.split(r'[\s.,;?!]+', text)
    return [word.lower() for word in words if len(word) > 5]