#coding:utf8
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm, AdminUser, MovieForm, Movie
from functools import wraps
from app import db
from werkzeug.utils import secure_filename
import os
import uuid
from app import app
import datetime


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = AdminUser.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误！')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
def logout():
    session.pop('admin', None)
    return redirect(url_for("admin.login"))


def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


@admin.route("/movie/add/", methods=['GET', 'POST'])
@admin_login_req
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        print(form.url.data)
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)
        if not os.path.exists(app.config['UP_DIR']):
            os.mkdir(app.config['UP_DIR'])

        url = change_filename(file_url)
        logo = change_filename(file_logo)
        form.url.data.save(os.path.join(app.config['UP_DIR'], url))
        form.logo.data.save(os.path.join(app.config['UP_DIR'], logo))

        data = form.data
        movie = Movie(
            title = data['title'],
            url = url,
            info = data['info'],
            logo = logo,
            speaker = data['speaker'],
            speaker_info = data['speaker_info']
        )
        db.session.add(movie)
        db.session.commit()
        flash('添加电影成功！', "ok")
        return redirect(url_for('admin.movie_add'))
    return render_template("admin/movie_add.html", form=form)


@admin.route("/movie/list/", methods=['GET'])
@admin_login_req
def movie_list():
    data = Movie.query.order_by(Movie.title).all()
    return render_template("admin/movie_list.html", data=data)


@admin.route("/movie/del/<string:title>", methods=['GET'])
@admin_login_req
def movie_del(title=None):
    movie = Movie.query.get_or_404(str(title))
    db.session.delete(movie)
    db.session.commit()
    flash('删除电影成功', 'ok')
    return redirect(url_for('admin.movie_list'))
