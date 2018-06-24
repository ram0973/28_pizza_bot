from flask import Response, request, current_app
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
from app.main.errors import HTTP_401


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', HTTP_401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def check_auth(username, password):
    return username == current_app.config['AUTH_USERNAME'] and \
           password == current_app.config['AUTH_PASSWORD']


class PizzaView(ModelView):
    def is_accessible(self):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            raise HTTPException('', authenticate())
        return True
