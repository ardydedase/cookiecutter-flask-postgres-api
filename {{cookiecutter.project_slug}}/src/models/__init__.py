# flake8: noqa
# TODO: check if there is a better way
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .abc import BaseModel
from .user import User

__all__ = ['BaseModel', 'User']
