from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .order import Order