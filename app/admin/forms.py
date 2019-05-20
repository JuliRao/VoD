# coding: utf8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, ValidationError
from app.models import AdminUser, Movie

class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label='id',
        validators=[
            DataRequired(u'请输入帐号！')
        ],
        description=u'帐号',
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入帐号！",
            "required": "required"
        }
    )

    pwd = PasswordField(
        label='passwd',
        validators=[
            DataRequired(u'请输入密码！')
        ],
        description=u'密码',
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码！",
            "required": "required"
        }
    )

    submit = SubmitField(
        u'登录',
        render_kw= {
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = AdminUser.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("帐号不存在！")


class MovieForm(FlaskForm):
    title = StringField(
        label='片名',
        validators=[
            DataRequired('请输入片名！')
        ],
        description='片名',
        render_kw={
            'class': 'form-control',
            'id': 'input_title',
            'placeholder': '请输入片名！'
        }
    )

    url = FileField(
        label='文件',
        validators=[
            DataRequired('请上传文件！'),
        ],
        description='文件',
        render_kw={
            'required': False
        }
    )

    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired('请输入简介！')
        ],
        description='简介',
        render_kw={
            'class': "form-control",
            'rows': "8",
            'cols': "100",
            'id': "input_info",
            'placeholder': '请输入片名！'
        }
    )

    logo = FileField(
        label='封面',
        validators=[
            DataRequired('请上传封面！')
        ],
        description='封面',
        render_kw={
            'required': False
        }
    )

    speaker = StringField(
        label='演讲者',
        validators=[
            DataRequired('请输入演讲者！')
        ],
        description='演讲者',
        render_kw={
            'class': 'form-control',
            'id': 'input_speaker',
            'placeholder': '请输入演讲者！'
        }
    )

    speaker_info = TextAreaField(
        label='演讲者信息',
        validators=[
            DataRequired('请输入演讲者信息！')
        ],
        description='演讲者信息',
        render_kw={
            'class': "form-control",
            'rows': "8",
            'cols': "92",
            'id': "input_speaker_info",
            'placeholder': '请输入演讲者信息！'
        }
    )

    submit = SubmitField(
        '添加',
        render_kw={
            'class': 'btn btn-primary'
        }
    )