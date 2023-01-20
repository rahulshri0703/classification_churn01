FROM python:3.8-slim-buster

WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN python setup.py install

CMD ["gunicorn","--bind","0.0.0.0:5000","flask_app.wsgi:app"]
