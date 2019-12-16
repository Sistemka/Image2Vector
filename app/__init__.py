from app.app import app
from app.handlers import (
    manage,
    errors
)

manage.register(app)
errors.register(app)
