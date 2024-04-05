FROM python:3.11-alpine 
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN rm /app/requirements.txt
COPY ./src /app/src
COPY ./main.py /app
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --reload