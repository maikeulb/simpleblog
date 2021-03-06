import os
import click
from glob import glob
from app.extensions import db
from app.models import User
from subprocess import call
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')

def register(app):

    @app.cli.command('init-db')
    @click.argument('username')
    @click.argument('password')
    @click.argument('email')
    def init_db(username, password, email):
        """Initialize the DB with a single user."""
        db.drop_all()
        db.create_all()
        admin = User(username, password, email)
        db.session.add(admin)
        db.session.commit()

    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')

    @app.cli.command("test")
    def test():
        import pytest
        rv = pytest.main([TEST_PATH, '--verbose'])
        exit(rv)


    @app.cli.command("lint")
    @click.option('-f', '--fix-imports', default=False, is_flag=True,
              help='Fix imports using isort, before linting')
    def lint(fix_imports):
        skip = ['node_modules', 'requirements', 'venv']
        root_files = glob('*.py')
        root_directories = [
            name for name in next(os.walk('.'))[1] if not name.startswith('.')]
        files_and_directories = [
            arg for arg in root_files + root_directories if arg not in skip]

        def execute_tool(description, *args):
            command_line = list(args) + files_and_directories
            click.echo('{}: {}'.format(description, ' '.join(command_line)))
            rv = call(command_line)
            if rv != 0:
                exit(rv)

        if fix_imports:
            execute_tool('Fixing import order', 'isort', '-rc')
        execute_tool('Checking code style', 'flake8')


    @app.cli.command("clean")
    def clean():
        for dirpath, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                if filename.endswith('.pyc') or filename.endswith('.pyo'):
                    full_pathname = os.path.join(dirpath, filename)
                    click.echo('Removing {}'.format(full_pathname))
                    os.remove(full_pathname)


    @app.cli.command("urls")
    @click.option('--url', default=None,
                  help='Url to test (ex. /static/image.png)')
    @click.option('--order', default='rule',
                  help='Property on Rule to order by (default: rule)')
    @with_appcontext
    def urls(url, order):
        rows = []
        column_length = 0
        column_headers = ('Rule', 'Endpoint', 'Arguments')

        if url:
            try:
                rule, arguments = (
                    current_app.url_map
                               .bind('localhost')
                               .match(url, return_rule=True))
                rows.append((rule.rule, rule.endpoint, arguments))
                column_length = 3
            except (NotFound, MethodNotAllowed) as e:
                rows.append(('<{}>'.format(e), None, None))
                column_length = 1
        else:
            rules = sorted(
                current_app.url_map.iter_rules(),
                key=lambda rule: getattr(rule, order))
            for rule in rules:
                rows.append((rule.rule, rule.endpoint, None))
            column_length = 2

        str_template = ''
        table_width = 0

        if column_length >= 1:
            max_rule_length = max(len(r[0]) for r in rows)
            max_rule_length = max_rule_length if max_rule_length > 4 else 4
            str_template += '{:' + str(max_rule_length) + '}'
            table_width += max_rule_length

        if column_length >= 2:
            max_endpoint_length = max(len(str(r[1])) for r in rows)
            max_endpoint_length = (
                max_endpoint_length if max_endpoint_length > 8 else 8)
            str_template += '  {:' + str(max_endpoint_length) + '}'
            table_width += 2 + max_endpoint_length

        if column_length >= 3:
            max_arguments_length = max(len(str(r[2])) for r in rows)
            max_arguments_length = (
                max_arguments_length if max_arguments_length > 9 else 9)
            str_template += '  {:' + str(max_arguments_length) + '}'
            table_width += 2 + max_arguments_length

        click.echo(str_template.format(*column_headers[:column_length]))
        click.echo('-' * table_width)

        for row in rows:
            click.echo(str_template.format(*row[:column_length]))
