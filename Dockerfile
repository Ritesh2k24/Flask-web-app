FROM Python:3.14.0a3-slim

WORKDIR /flaskapp

COPY app.py requirements.txt /flaskapp/

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]