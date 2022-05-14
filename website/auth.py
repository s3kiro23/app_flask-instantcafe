from flask import Blueprint, render_template, request, redirect, url_for, flash

# from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pseudo = request.form.get("email")
        password = request.form.get("password")
    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        pseudo = request.form.get("pseudo")
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if password == password2:
            flash("Compte créé avec succés", category="success")
            return render_template("views.hello")
        flash("Les mots de passe ne correspondent pas !", category="denied")
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return render_template(url_for("auth.login"))
