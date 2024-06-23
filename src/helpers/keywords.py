def extract_keywords(text):
    words = text.split(" ")
    return [word.lower() for word in words if len(word) > 4]