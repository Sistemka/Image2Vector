from app.app import api
from app.handlers import (
    manage,
    errors
)

manage.register(api)
errors.register()
