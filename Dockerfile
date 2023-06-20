FROM python:3.9

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]