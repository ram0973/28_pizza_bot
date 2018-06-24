from flask import render_template
from flask_wtf.csrf import CSRFError

from app.main.views import main

HTTP_400 = 400
HTTP_401 = 401
HTTP_403 = 403
HTTP_404 = 404
HTTP_451 = 451
HTTP_500 = 500


@main.app_errorhandler(HTTP_403)
def forbidden(_):
    return render_template('errors/403.html'), HTTP_403


@main.app_errorhandler(HTTP_404)
def page_not_found(_):
    return render_template('errors/404.html'), HTTP_404


@main.app_errorhandler(HTTP_451)
def internal_server_error(_):
    return render_template('errors/451.html'), HTTP_451


@main.app_errorhandler(HTTP_500)
def internal_server_error(_):
    return render_template('errors/500.html'), HTTP_500


@main.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/csrf.html', csrf_error=e.description), \
           HTTP_400
