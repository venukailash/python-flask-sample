from config import db
from src.models.person import Person

class PersonService:
    def get_all():
        return Person.query.all()
    
    @staticmethod
    def create(person):
        existing_person = Person.query.filter(Person.lname == person.lname).one_or_none()

        if existing_person is None:
            db.session.add(person)
            db.session.commit()
            return person
        else:
            raise ValueError(f"Person with last name {person.lname} already exists")
        
    @staticmethod   
    def read_one(lname):
        existing_person = Person.query.filter(Person.lname == lname).one_or_none()

        if not existing_person:
            raise ValueError(f"Person with last name {lname} not found")
        return existing_person

    @staticmethod
    def update(lname, person):
        existing_person = Person.query.filter(Person.lname == lname).one_or_none()
        
        if not existing_person:
            raise ValueError(f"Person with last name {lname} not found")
        
        existing_person.fname = person.fname
        db.session.commit()
        return existing_person
        
    @staticmethod    
    def remove(lname):
        existing_person = Person.query.filter(Person.lname == lname).one_or_none()

        if not existing_person:
            raise ValueError(f"Person with last name {lname} not found")
        
        db.session.delete(existing_person)
        db.session.commit()
