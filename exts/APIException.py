import json

from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self,status=500, msg=None, error_code=10000):
        if status:
            self.code = status
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
