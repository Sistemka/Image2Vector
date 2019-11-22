from functools import wraps

from flask import request, jsonify

from settings.config import ALLOWED_MIMETYPE


def check_mimetype():
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if request.files.get('image').content_type not in ALLOWED_MIMETYPE:
                response = jsonify({
                    'result': [],
                    'error': True,
                    'message': 'Not allowed mimetype'
                })
                response.status_code = 400
                return response
            return func(*args, **kwargs)
        return decorated_function
    return decorator
