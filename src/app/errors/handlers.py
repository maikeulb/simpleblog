from flask import render_template
from app.errors import bp

class Error(object):
    def __init__(self, error_code, error_title):
        self.code = error_code
        self.title = error_title


@bp.app_errorhandler(400)
def bad_request(e):
    error = Error(400, "Bad Request")
    return render_template("errorpage.html", data=error), 400


@bp.app_errorhandler(401)
def unauthorized(e):
    error = Error(401, "Unauthorized")
    return render_template("errorpage.html", data=error), 401


@bp.app_errorhandler(403)
def forbidden(e):
    error = Error(403, "Forbidden")
    return render_template("errorpage.html", data=error), 403


@bp.app_errorhandler(404)
def page_not_found(e):
    error = Error(404, "Page Not Found")
    return render_template('error_page.html', error=error), 404


@bp.app_errorhandler(418)
def teapot(e): 
    error = Error(418, "I'm a Teapot")
    return render_template('error_page.html', error=error), 418


@bp.app_errorhandler(500)
def server_error(e):
    error = Error(500, "Internal Server Error")
    return render_template("error_page.html", data=error), 500


@bp.app_errorhandler(502)
def bad_gateway(e):
    error = Error(502, "Bad Gateway")
    return render_template("error_page.html", data=error), 502


@bp.app_errorhandler(503)
def gateway_timeout(e):
    error = Error(503, "Gateway Timeout")
    return render_template("error_page.html", data=error), 503
