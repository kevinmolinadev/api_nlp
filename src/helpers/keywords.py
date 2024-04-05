import re
def extract_keywords(text):
    # List of words to omit
    omit_words = ['claro', 'unos', 'unas', 'cómo', 'cuándo', 'cuál', 'cuáles', 'quién', 'tengo', 'llamo', 'llame', 'estar', 'tener', 'encuentra', 'tiene', 'cuántos', 'cuántas', 'quiénes', 'este', 'para', 'podamos', 'todos', 'cuantas', 'cuales', 'solo', 'quiero', 'están', 'quien']
    # Build the regular expression pattern
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, omit_words)) + r')\b|\b\w+\b', flags=re.IGNORECASE)
    # words = text.split(" ");
    # Find all keywords in the text
    keywords = [word.lower() for word in pattern.findall(text) if word.lower() not in omit_words and len(word) > 3]
    if len(keywords) > 0:
        return keywords
    else:
        return False