from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, DateTime

db = SQLAlchemy()


class MyModel(db.Model):
    id = Column(Integer, primary_key=True)
    some_string = Column(Unicode)
    some_integer = Column(Integer)
    some_time = Column(DateTime, default=datetime.now)