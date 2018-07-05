FROM python:3.6

WORKDIR /worker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]