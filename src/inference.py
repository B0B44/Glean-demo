import os
import uuid
from typing import List
from urllib.parse import urlparse

import PIL.Image
import boto3
import pdf2image
import pytesseract
from flask_restful import Resource, reqparse
from pdf2image import convert_from_path

s3_client = boto3.client('s3')
parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('s3_uri',
                    type=str,
                    required=True)


class Inference(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        args = parser.parse_args()

        parsed = urlparse(args['s3_uri'], allow_fragments=False)
        bucket_name: str = parsed.netloc
        obj_key: str = parsed.path[1:]

        file_ext: str = obj_key.split('.')[-1]
        file_is_pdf: bool = 'pdf' in file_ext.lower()
        storage_key: str = f'{uuid.uuid4().hex}.{file_ext}'
        file_keys: List[str] = []

        try:
            s3_client.download_file(bucket_name, obj_key, storage_key)

            if not file_is_pdf:
                file_keys.append(storage_key)
            else:
                pages: List[PIL.Image.Image] = pdf2image.convert_from_path(storage_key, 500)
                for page in pages:
                    page_storage_key: str = f'{uuid.uuid4().hex}.png'
                    file_keys.append(page_storage_key)
                    page.save(page_storage_key, 'PNG')

            result: List[str] = []
            for file_key in file_keys:
                result.append(pytesseract.image_to_string(file_key))

            return '\n'.join(result)

        finally:
            file_keys.append(storage_key)
            for file_key in file_keys:
                if os.path.exists(file_key):
                    os.remove(file_key)
