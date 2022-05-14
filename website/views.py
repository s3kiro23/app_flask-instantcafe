from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def hello():
    return render_template("home.html")


@views.route("/contact")
def contact():
    return render_template("contact.html")


@views.route("/apropos")
def apropos():
    return render_template("apropos.html")


@views.route("/cgu")
def cgu():
    return render_template("cgu.html")


@views.route("/blog")
def blog():
    return render_template("blog.html")
