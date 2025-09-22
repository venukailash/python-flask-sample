from extensions import db
from src.models.user import User
from sqlalchemy.exc import DBAPIError

class UserService:
    @staticmethod
    def get_all():
        return User.query.all()
    