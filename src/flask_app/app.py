from flask import Flask, request, jsonify, render_template, Blueprint
from admin import admin
from flask_restful import Resource, Api


app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')

api = Api(app)
# http://127.0.0.1:5000/admin


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)


'''
run:
for linux n unix : export FLASK_APP=flask_app/app.py
for windows: set FLASK_APP=flask_app/app.py
for powershell : $FLASK_APP=flask_app/app.py

flask run --host=0.0.0.0 --port=5000



'''
