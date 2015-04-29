from flask import Flask
from models import db
from rest_api import register_rest_api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprints(app):
    from views import my_view

    app.register_blueprint(my_view)




if __name__ == '__main__':
    app = create_app('config.Config')
    register_blueprints(app)
    register_rest_api(app)
    app.run(debug=True, threaded=True, port=5678, host='0.0.0.0')
