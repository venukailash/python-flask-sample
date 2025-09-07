from src.services.person_service import PersonService
from src.schemas.person_schema import people_schema, person_schema
from flask import abort

def read_all():
    people = PersonService.get_all()
    return people_schema.dump(people), 200

def create(person):
    try:
        created_person = PersonService.create(person_schema.load(person))
        return person_schema.dump(created_person)
    except ValueError as e:
        abort(406, e.args)
    
def read_one(id):
    try:
        person = PersonService.read_one(id=id)
        return person_schema.dump(person)
    except ValueError as e:
        abort(404, e.args)

def update(id, person):
    try:
        person_to_update = person_schema.load(person)
        updated_person = PersonService.update(id=id, person=person_to_update)
        return person_schema.dump(updated_person)
    except ValueError as e:
        abort(404, e.args)

def remove(id):
    try:
        PersonService.remove(id=id)
        return f"Person {id} deleted", 200
    except ValueError as e:
        abort(404, e.args)