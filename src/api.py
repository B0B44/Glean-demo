from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from inference import Inference


def main():
    app = Flask(__name__)
    CORS(app, resources={r'/inference': {'origins': '*'}})
    api = Api(app)

    api.add_resource(Inference, '/inference')
    app.run(host='0.0.0.0', port=80)

