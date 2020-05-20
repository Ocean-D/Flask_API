

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, jsonify

api = Redprint('token')
@api.route('',methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
        # ClientTypeEnum.USER_MOBILE: '',
        # ClientTypeEnum.USER_MAIN:'',
        # ClientTypeEnum.USER_WX:''
        }

    identify = promise[form.type.data](
        form.account.data,
        form.secret.data
    )
    token = generate_token(identify['uid'],
                   form.type.data,
                   identify['scope'],
                   current_app.config['TOKEN_EXPIRATION'])
    t = {
        'token':token.decode('ascii')
    }
    return jsonify(t),201


def generate_token(uid,ac_type,scope=None,expiration=7200):
    '''生成令牌'''
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps(
        {'uid':uid,
         'type':ac_type.value,
         'scope':scope}
    )
