import config
import os

from flask import Flask, render_template
from app import commands, models
import app.models
from app.account import account as account_bp
from app.extensions import bcrypt, cache, csrf_protect, db, debug_toolbar, login, migrate
from app.main import main as main_bp

Config = eval(os.environ['FLASK_APP_CONFIG'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    # cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(account_bp, url_prefix='/account')
    # app.register_blueprint(errors_bp)
    app.register_blueprint(main_bp)
    return None

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)

# def configure_template_filters(app):
#     app.jinja_env.filters["pretty_date"] = pretty_date
#     app.jinja_env.filters["format_date"] = format_date
#     app.jinja_env.filters["nl2br"] = nl2br

def register_shellcontext(app):
    def shell_context():
        return {
            'db': db,
            'User': models.User}
    app.shell_context_processor(shell_context)
