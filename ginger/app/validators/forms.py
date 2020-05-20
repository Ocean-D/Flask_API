from wtforms import  StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, length, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired()
                                      ,Length(min=5,max=32)])
    secret = StringField()

    type = IntegerField(validators=[DataRequired()])


    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    nickname = StringField(validators=[DataRequired(),
                                           length(min=2, max=22)])

    account = StringField(validators=[DataRequired(),
        Email(message='invalidate email')
    ])

    secret = StringField(validators=[
            DataRequired(),
            # password can only include letters , numbers and "_"
            Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
        ])


    def validate_account(self,value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
    def validate_nickname(self,value):
        if User.query.filter_by(nickname = value.data).first():
            raise ValidationError()


class SearchForm(BaseForm):
    q = StringField(validators=[DataRequired()])