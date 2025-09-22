from src.services.user_service import UserService
from src.schemas.user_schema import users_schema

def read_all():
    users = UserService.get_all()
    return users_schema.dump(users), 200
