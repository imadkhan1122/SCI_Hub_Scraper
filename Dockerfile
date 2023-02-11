FROM python:3.8.3-alpine

COPY . /

RUN pip install --upgrade pip

RUN adduser -D myuser
USER myuser

RUN pip install -r requirements.txt

CMD [ "python3", "GetPaper.py" ]
