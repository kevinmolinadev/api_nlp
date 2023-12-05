import re
"""""
this method receives an array with the contexts, it also receives the keyword to filter the contexts for the specific questions 
```python
    data = ['first context','second context']
    keywords = ['first']
    extract_context(data,keywords) // ==> 'first context'
```
"""
def extract_context(data, keywords):
    context = ''
    for item in data:
        lower_question = str(item.question).lower()
        keyword_matches = sum(keyword in lower_question for keyword in keywords)
        if keyword_matches == 0: continue
        threshold = len(keywords) -1 
        if keyword_matches >= threshold:
            context += f"{str(item.context).strip()}.\n\n\n"
    return context