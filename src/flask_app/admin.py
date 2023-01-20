from flask import Flask, Blueprint
from flask import request, jsonify, render_template

admin = Blueprint('admin', __name__)


@admin.route('/greeting')
def greeting():
    return 'Hello, administrative user!'


@admin.route('/')
def index():
    return render_template("index.html")


@admin.route('/health')
def health():
    d = {'check': 200}
    return jsonify(d)
