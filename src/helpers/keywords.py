import re
def extract_keywords(text):
    # List of words to omit
    omit_words = ['claro','el', 'la', 'los', 'las', 'de', 'en', 'un', 'una', 'unos', 'unas', 'y', 'o', 'es', 'son', 'cómo', 'cuándo', 'cuál', 'cuáles', 'quién', 'qué', 'tengo','me','llamo','llame','ser','estar','tener','hay','fue','mi','se', 'encuentra', 'tiene', 'cuántos', 'cuántas', 'quiénes', 'este', 'para', 'que', 'podamos', 'todos', 'cuantas', 'cuales']
    # Build the regular expression pattern
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, omit_words)) + r')\b|\b\w+\b', flags=re.IGNORECASE)
    # Find all keywords in the text
    keywords = [word.lower() for word in pattern.findall(text) if word.lower() not in omit_words]
    if len(keywords) > 0:
        return keywords
    else:
        return False