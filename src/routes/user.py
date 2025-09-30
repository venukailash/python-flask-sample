from marshmallow.exceptions import ValidationError
from src.services.user_service import UserService
from src.schemas.user_schema import users_schema, user_schema
from flask import abort

def read_all():
    users = UserService.get_all()
    return users_schema.dump(users), 200

def get_one(email):
    try:
        user = UserService.get_one(email)
        return user_schema.dump(user), 200
    except ValidationError as e:
        abort(400, {"error": "Validation failed", "details": e.args})
    except ValueError as e:
        abort(404, {"error": "Invalid request", "message": str(e)})
