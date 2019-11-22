from flask import request
from werkzeug.exceptions import HTTPException

from app import api


@api.errorhandler(HTTPException)
def http_exception(e):
    response = {
        'message': str(e),
        'error': True,
        'request_id': request.headers.get('X-REQUEST-ID')
    }
    return response, getattr(e, 'code', 500)


@api.errorhandler(Exception)
def application_exception(e):
    response = {
        'message': str(e),
        'error': True,
        'request_id': request.headers.get('X-REQUEST-ID')
    }
    return response, getattr(e, 'code', 500)


def register():
    pass
