import os
from pathlib import Path

from aiohttp import web
from aiofiles.os import wrap

from src import image_to_vector_process
from settings.path import FILES_DIR


async def handler_image_to_vector(request):
    reader = await request.multipart()
    field = await reader.next()
    results = []
    while field is not None:
        image_name = field.filename
        image_path = Path(FILES_DIR, image_name)
        with open(image_path, 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                f.write(chunk)
        field = await reader.next()
        result = image_to_vector_process(image_path).tolist()
        results.append(result)
        wrap(os.remove(image_path))

    return web.json_response({
        'error': False,
        'result': results
    })


def register(app):
    app.add_routes([web.post('/image2vector', handler_image_to_vector)])
