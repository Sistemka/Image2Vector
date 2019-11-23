import os
from pathlib import Path

from flask import jsonify
from flask_restplus import Resource, Namespace
from werkzeug.utils import secure_filename

from app.app import basic_args, image_args
from src import image2vector
from settings.path import FILES_DIR
from utils.check_mimetype import check_mimetype

ns = Namespace(
    '',
    description='Image2Vector',
    validate=True
)


@ns.route('/image2vector')
@ns.expect(basic_args)
class Image2Vector(Resource):
    @ns.expect(image_args)
    @check_mimetype()
    def post(self):
        basic_args.parse_args()
        args = image_args.parse_args()
        image = args['image']
        size = (args.get('width'), args.get('height'))
        image_name = secure_filename(image.filename)
        image_path = Path(FILES_DIR, image_name).as_posix()
        image.save(image_path)
        res = image2vector(image_path=image_path, size=size)
        os.remove(image_path)
        return jsonify({
            'error': False,
            'result': res
        })


def register(main_api):
    main_api.add_namespace(ns)
