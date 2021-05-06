from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r42c898914'

    from .app_server import APP_SERVER_BLUEPRINT
    app.register_blueprint(APP_SERVER_BLUEPRINT)

    return app
