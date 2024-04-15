import re
"""""
this method receives an array with the contexts, it also receives the keyword to filter the contexts for the specific questions 
```python
    data = ['first context','second context','second context','second context','second context','second context']
    keywords = ['first']
    extract_context(data,keywords) // ==> 'first context'
```
"""
def extract_context(data, keywords):
    context = []
    for item in data:
        lower_question = str(item.question).lower()
        #4 estudio ingeniería sistemas informáticos
        keyword_matches = sum(keyword in lower_question for keyword in keywords)
        if keyword_matches == 0: continue
        if (keyword_matches>=int(len(keywords)/2)):
            context.append(f"{str(item.context).strip()}")
    return context