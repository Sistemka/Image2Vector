from asyncio import CancelledError

from aiohttp import web


async def http_exception(request, e):
    data = {
        'message': str(e),
        'error': True,
        'request_id': request.headers.get('X-REQUEST-ID')
    }
    return web.json_response(data=data, status=e.status)


async def application_exception(request, e):
    data = {
        'message': str(e),
        'error': True,
        'request_id': request.headers.get('X-REQUEST-ID')
    }
    return web.json_response(data=data, status=getattr(e, 'code', 500))


def create_error_middleware():
    @web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)
            return response
        except CancelledError:
            pass
        except web.HTTPException as e:
            return await http_exception(request, e=e)
        except Exception as e:
            return await application_exception(request, e=e)
    return error_middleware


def register(app):
    error_middleware = create_error_middleware()
    app.middlewares.append(error_middleware)
