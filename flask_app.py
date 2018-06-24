import os
import pprint
from flask.cli import AppGroup
from flask_admin import Admin, AdminIndexView
from app import create_app, db
from app.auth import PizzaView
from app.bot import pizza_catalog_bot
from app.models import Pizza, Size

app = create_app(os.getenv('FLASK_ENV') or 'default')

admin = Admin(app, index_view=AdminIndexView(name='Pizza Store Admin', url='/'))
admin.add_view(PizzaView(Pizza, db.session))
admin.add_view(PizzaView(Size, db.session))


@app.shell_context_processor
def make_shell_context():
    """ make all these available in flask shell. usage: flask shell """
    return dict(app=app, db=db, Pizza=Pizza, Size=Size, pprint=pprint.pprint)


@app.cli.command()
def tests():
    """Cli command: flask tests"""
    import unittest

    app_tests = unittest.TestLoader().discover('app.tests')
    unittest.TextTestRunner(verbosity=2).run(app_tests)


db_cli = AppGroup('database')


@db_cli.command('init')
def init_database():
    """ Cli command: flask database init """
    db.drop_all()
    db.create_all()
    db.session.commit()


@db_cli.command('seed')
def seed_database():
    """ Cli command: flask database seed """
    from app.models.seeds import pizzas, sizes
    db.session.bulk_insert_mappings(Size, sizes)
    db.session.bulk_insert_mappings(Pizza, pizzas)
    db.session.commit()


app.cli.add_command(db_cli)


@app.cli.command()
def telegram_bot():
    """ Cli command: flask telegram_bot """
    pizza_catalog_bot()