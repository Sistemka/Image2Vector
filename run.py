from app.app import app
from aiohttp.web import run_app

if __name__ == '__main__':
    run_app(app, port=5005)
