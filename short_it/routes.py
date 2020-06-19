from flask import render_template, url_for, jsonify, redirect, request, flash
from short_it import app, db, bcrypt
from short_it.models import URL, User
from short_it.forms import LoginForm, RegistrationForm, ShortenForm


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return render_template("home.html", title="Home")


@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    form = ShortenForm()

    if request.method == "POST" and form.validate_on_submit():
        pass

    return render_template("shorten.html", title="Short-It", form=form)


@app.route("/<string:url_id>")
def shortened(url_id):
    return url_id


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
        return redirect(url_for("index"))

    return render_template("register.html", title="Register", form=form)
