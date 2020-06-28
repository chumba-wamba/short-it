from flask import render_template, url_for, jsonify, redirect, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
from short_it import app, db, bcrypt
from short_it.models import URL, User
from short_it.forms import LoginForm, RegistrationForm, ShortenForm, ShareForm, AccountForm
from short_it.shortener import random_url_gen


# Route for home page
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    # If the user is already logged in and
    # hence has user id stored in the session,
    # then we redirect this individual back to
    # index page
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("home.html", title="Home")


# Rotue for shorten page
@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    # create oboject of the WTForm to be used
    # by end users to add in the original and
    # the (optional) shortened URL
    form = ShortenForm()

    # Handling POST requests; in this case the
    # only POST request to be recieved is that
    # of a form submission
    # Hence all other POST requests will return
    # and render the default web page for the route
    if request.method == "POST" and form.validate_on_submit():
        # This block of code checks whether the
        # form data entered by the user has the
        # optional shortened url data or not
        # If it does not have the shortened url data,
        # then it is generated by the random_url_gen function
        if not form.shortened_url.data:
            shortened_url = random_url_gen()
        else:
            shortened_url = form.shortened_url.data

        # Since any individual can shorten any link they
        # want, but only registered users can access
        # information such as user hits, user locations, etc.
        # relevant to the shortened URLs, this block of code
        # checks whether a session has a user logged in or not
        # If a user is logged in, then the ID of the User object
        # is stored in a field of the document belonging to the
        # shortened URL that is going to be generated
        owner = None
        if current_user.is_authenticated:
            owner = current_user.id

        # Creating an URL object to store the
        # original url data (recieved from the WTForm)
        # along with the shortened url data
        new_shortened_url = URL(
            original_url=form.original_url.data,
            shortened_url=shortened_url,
            owner=owner
        )
        new_shortened_url.save()  # Adding the URL object to the database

        flash("localhost:5000/"+str(shortened_url), "primary")
    return render_template("shorten.html", title="Short-It", form=form)


# Rotue for redirecting a shortened URL call
# to the original URL
@app.route("/<string:url_id>")
def shortened(url_id):
    # This block of code redirects the end user
    # to the desired location, if there exists a
    # short => long mapping
    # Otherwise, a flash message is generated

    # NOTE: Try generating a custom error page
    # rather than a flash message (Take someone's
    # opinion regarding this idea)
    objects = URL.objects(shortened_url=url_id)
    if len(objects) == 1:
        url_object = objects[0]
        url_object.update(inc__counter=1)
        url_object.update(push__date_array=datetime.utcnow)
        original_url = url_object.original_url
        return redirect(original_url)

    flash("The URL does not exist", "danger")
    return redirect(url_for("index"))


# Rotue to access the dashboard which
# stores all the information pertaining
# to shortened URLs
# Is only accessible by registered users
@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    # TODO: Acquire information for all the
    # links belonging to the end user and display
    # these stats

    form = ShareForm()
    url_list = URL.objects(owner=current_user.id)

    shared_id_list = User.objects(
        id=current_user.id).first().shared_url_list

    shared_list = []
    for url_id in shared_id_list:
        shared_list.append(URL.objects(id=url_id).first())

    return render_template("dashboard.html", title="Dashboard", form=form, url_list=url_list, shared_list=shared_list)


@app.route("/share/<string:url_id>", methods=["GET", "POST"])
@login_required
def share(url_id):
    form = ShareForm()
    if request.method == "POST" and form.validate_on_submit():
        object_list = User.objects(user_name=form.user_name.data)
        if len(object_list) == 0:
            flash("The user name does not exist.", "danger")
            return redirect(url_for("dashboard"))

        if len(object_list) == 1 and object_list[0].user_name == User.objects(id=current_user.id).first().user_name:
            flash("Enter a username that is not the same as yours :P", "danger")
            return redirect(url_for("dashboard"))

        if url_id in User.objects(user_name=form.user_name.data).first().shared_url_list:
            flash(
                f"Shortened URL information has already been shared with the {form.user_name.data}", "warning")
            return redirect(url_for("dashboard"))

        object_list.first().update(push__shared_url_list=url_id)
        flash(
            f"Shared shortened URL information with {form.user_name.data}", "success")

    return redirect(url_for("dashboard"))


# Rotue to access the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # If the user is already logged in and
    # hence has user id stored in the session,
    # then we redirect this individual back to
    # index page
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    # create oboject of the WTForm to be used
    # by end users to add in the original and
    # the (optional) shortened URL
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # Acquire user object based on form data
        user = User.objects(user_name=form.user_name.data)
        if len(user) == 1 and bcrypt.check_password_hash(user.first().password, form.password.data):
            # if information matches, log the user in
            login_user(user=user.first())
            flash("You were successfully logged in!", "success")

            # If the login is a result of a redirection due to
            # end user trying to access a route with login required,
            # we redirect the user to that initial route
            if request.args.get('next'):
                return redirect(request.args.get('next'))

            return redirect(url_for("index"))
        flash("Login unsuccessful", "danger")

    return render_template("login.html", title="Login", form=form)


# Rotue to access the registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        print(type(hashed_password))
        print(hashed_password)

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            user_name=form.user_name.data,
            email=form.email.data,
            password=hashed_password,
        )
        new_user.save()

        flash(
            f"Welcome, {form.user_name.data}! You have been successfully registered as a user of Short It :)", "success")
        return redirect(url_for("index"))

    return render_template("register.html", title="Register", form=form)


# Route to access and update the account
# details of the user
@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = AccountForm()
    user = User.objects(id=current_user.id).first()

    if request.method == "POST" and form.validate_on_submit():
        changes = []
        if form.first_name.data:
            user.update(set__first_name=form.first_name.data)
            changes.append("First Name")
        if form.last_name.data:
            user.update(set__last_name=form.last_name.data)
            changes.append("Last Name")
        if form.password.data and bcrypt.check_password_hash(user.password, form.password.data) and form.new_password.data == form.confirm_new_password.data:
            hashed_password = bcrypt.generate_password_hash(
                form.new_password.data).decode('utf-8')
            user.update(password=hashed_password)
            changes.append("Password")

        change_message = "Updated: "+", ".join(changes)
        flash(change_message, "info")
        return redirect(url_for("account"))

    return render_template("account.html", title="Account", form=form, user=user)

# Rotue to logout the user and delete
# the session
@app.route("/logout")
def logout():
    logout_user()
    flash("You were successfully logged out!", "success")
    return redirect(url_for("index"))
