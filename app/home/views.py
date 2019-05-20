#coding:utf8
from . import home
from flask import render_template
from app.admin.forms import Movie


@home.route("/")
def index():
    data = Movie.query.order_by(Movie.title).all()#.paginate(page=1, per_page=100)
    return render_template("home/index.html", data=data)


@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


@home.route("/play/<string:title>/")
def play(title=None):
    movie = Movie.query.get_or_404(str(title))
    return render_template('home/play.html', movie=movie)
