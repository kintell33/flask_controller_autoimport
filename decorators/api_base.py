from functools import wraps

from exceptions.exception_authorization_error import AuthorizationError
from exceptions.exception_validation_error import ValidationError
from flask import jsonify, request
import traceback


class api():
    def authorization(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.headers.get('Authorization')

            try:
                return f(*args, **kwargs)
            except AuthorizationError as error:
                return jsonify({"status": "authorization-error", "message": str(error)}), 403

        return decorated_function

    def exception(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except ValidationError as error:
                return jsonify({"status": "validation-error", "message": str(error)}), 400
            except Exception as error:
                tb = traceback.format_exc()
                return jsonify({"status": "server-error", "message": str(type(error)) + ' - ' + str(error) + ' - ' + tb }), 500
        return decorated_function
