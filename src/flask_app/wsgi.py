from flask_app.restapi import app

if __name__ == "__main__":
    app.run()

# gunicorn --bind 0.0.0.0:5000 wsgi:app
# gunicorn --workers 3 --bind 0.0.0.0:5000 -m 777 wsgi:app
# run from outside dir: unicorn --bind 0.0.0.0:5000 flask_app.wsgi:app
