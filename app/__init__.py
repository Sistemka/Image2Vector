from app.app import app, api
from app.handlers import (
    manage,
    errors
)

manage.register(api)
errors.register()
