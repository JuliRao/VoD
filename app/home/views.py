#coding:utf8
from . import home
from flask import render_template


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


@home.route("/search/")
def search():
    return render_template("home/search.html")


@home.route("/play/")
def play():
    return render_template("home/play.html")