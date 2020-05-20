from werkzeug.exceptions import  HTTPException

from app import create_app

from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()
# @app.app_errorhandler()
@app.errorhandler(Exception)
def framework_error(e):
    #APIException
    #HTTPException
    #Exception
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code=code,msg=msg,error_code=error_code)
    else:
        #调试模式
        #log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e




if __name__ == '__main__':
    app.run('0.0.0.0',debug=app.config['DEBUG'])