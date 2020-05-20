from flask import request
from app.libs.error_code import ClientTypeError, Success

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm,UserEmailForm

api = Redprint('client')

@api.route('/register',methods=['POST'])
def client():
    #如果是json就用关键字
    # data = request.json
    form = ClientForm().validate_for_api()
    promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email,
            # ClientTypeEnum.USER_MOBILE: '',
            # ClientTypeEnum.USER_MAIN:'',
            # ClientTypeEnum.USER_WX:''
        }
    promise[form.type.data]()
    return  Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,form.account.data,form.secret.data)