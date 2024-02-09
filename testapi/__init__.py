import os
from flask import Flask
from flask_restful import Api
from .routers import initialize_routes


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="Projeto de teste",
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app)
    initialize_routes(api)
    return app
