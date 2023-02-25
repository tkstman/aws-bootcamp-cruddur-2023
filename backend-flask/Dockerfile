FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}

#HEALTHCHECK CMD curl --fail http://localhost:4567/ || exit 1

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567" ]
