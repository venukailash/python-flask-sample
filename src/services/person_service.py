from config import db
from src.models.person import Person

class PersonService:
    def get_all():
        return Person.query.all()
    
    @staticmethod
    def create(person):
        db.session.add(person)
        db.session.commit()
        return person
        
    @staticmethod   
    def read_one(id):
        existing_person = Person.query.get(id)

        if not existing_person:
            raise ValueError(f"Person with id {id} not found")
        return existing_person

    @staticmethod
    def update(id, person):
        existing_person = Person.query.get(id)
        
        if not existing_person:
            raise ValueError(f"Person with id {id} not found")
        
        existing_person.fname = person.fname
        existing_person.lname = person.lname
        db.session.commit()
        return existing_person
        
    @staticmethod    
    def remove(id):
        existing_person = Person.query.get(id)

        if not existing_person:
            raise ValueError(f"Person with id {id} not found")
        
        db.session.delete(existing_person)
        db.session.commit()
