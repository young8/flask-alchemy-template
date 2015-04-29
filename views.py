from flask import Blueprint, render_template
from models import MyModel


my_view = Blueprint('my_view', __name__, template_folder="templates")

@my_view.route('/')
def index():
    all_data = MyModel.query.all()
    return render_template('index.html', data=all_data)

