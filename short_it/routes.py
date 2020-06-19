from flask import render_template, url_for, jsonify, redirect, request, flash
from short_it import app, db, bcrypt
from short_it.models import URL, User
from short_it.forms import LoginForm, RegistrationForm, ShortenForm
from short_it.shortener import random_url_gen


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return render_template("home.html", title="Home")


@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    form = ShortenForm()

    if request.method == "POST" and form.validate_on_submit():
        if not form.shortened_url.data:
            shortened_url = random_url_gen()
        else:
            shortened_url = form.shortened_url.data

        new_shortened_url = URL(
            original_url=form.original_url.data,
            shortened_url=shortened_url,
        )
        new_shortened_url.save()
        flash("localhost:5000/"+str(shortened_url), "primary")
    return render_template("shorten.html", title="Short-It", form=form)


@app.route("/<string:url_id>")
def shortened(url_id):
    objects = URL.objects(shortened_url=url_id)
    if len(objects) == 1:
        original_url = objects[0].original_url
        return redirect(original_url)

    flash("The URL does not exist", "danger")
    return redirect(url_for("index"))


@app.route("/dashboard/<string:url_id>")
def dashboard(url_id):
    return url_id


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        login_user = User.objects(user_name=form.user_name.data)
        if len(login_user) == 1 and bcrypt.check_password_hash(login_user[0].password, form.password.data):
            flash("You were successfully logged in!", "success")
            return redirect(url_for("index"))
        flash("Login unsuccessful", "danger")

    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data)

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            user_name=form.user_name.data,
            email=form.email.data,
            password=hashed_password,
        )
        new_user.save()

        flash(f"Welcome, {form.user_name.data}!", "success")
        return redirect(url_for("index"))

    return render_template("register.html", title="Register", form=form)
