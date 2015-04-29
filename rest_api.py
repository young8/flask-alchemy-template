from flask.ext.restless import APIManager
from models import db, MyModel


def register_rest_api(app):
    manager = APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(MyModel, methods=['GET', 'POST'], url_prefix='/api')