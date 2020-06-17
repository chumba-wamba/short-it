from flask import render_template, url_for, jsonify, redirect
from short_it import app
from short_it.models import URL, User


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return "Hello, world!\n"


@app.route("/<string:url_id>")
def shortened(url_id):
    return url_id


@app.route("/dashboard/<string:url_id>")
def dashboard(url_id):
    return url_id
