from flask import Blueprint

APP_SERVER_BLUEPRINT = Blueprint('app_server', __name__)
ERROR_HANDLER_BLUEPRINT = Blueprint("error_handler", __name__)

from . import routes