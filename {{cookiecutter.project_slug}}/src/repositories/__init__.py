from flask_sqlalchemy import SQLAlchemy
from .user import UserRepository


db = SQLAlchemy()
__all__ = ['UserRepository']
