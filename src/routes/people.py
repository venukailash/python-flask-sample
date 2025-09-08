from src.services.person_service import PersonService
from src.schemas.person_schema import people_schema, person_schema
from flask import abort
from marshmallow.exceptions import ValidationError

def read_all():
    people = PersonService.get_all()
    return people_schema.dump(people), 200

def create(person):
    try:
        created_person = PersonService.create(person_schema.load(person))
        return person_schema.dump(created_person), 201
    except ValidationError as e:
        abort(400, {"error": "Validation failed", "details": e.args})
    except ValueError as e:
        abort(400, {"error": "Invalid request", "message": str(e)})
    
def read_one(id):
    try:
        person = PersonService.read_one(id=id)
        return person_schema.dump(person)
    except ValueError as e:
        abort(404, {"error": "Invalid request", "message": str(e)})

def update(id, person):
    try:
        person_to_update = person_schema.load(person)
        updated_person = PersonService.update(id=id, person=person_to_update)
        return person_schema.dump(updated_person)
    except ValidationError as e:
        abort(400, {"error": "Validation failed", "details": e.messages})
    except ValueError as e:
        if "not found" in str(e).lower():
            abort(404, {"error": str(e)})
        else:
            abort(400, {"error": str(e)})

def remove(id):
    try:
        PersonService.remove(id=id)
        return f"Person {id} deleted", 200
    except ValueError as e:
        abort(404, {"error": "Invalid request", "message": str(e)})