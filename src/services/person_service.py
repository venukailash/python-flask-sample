from config import db
from src.models.person import Person
from sqlalchemy.exc import DBAPIError

class PersonService:
    @staticmethod
    def get_all():
        return Person.query.all()
    
    @staticmethod
    def create(person):
        try:
            if not person.fname or not person.lname:
                raise ValueError("First name and last name are required")

            existing_person = Person.query.filter_by(fname=person.fname, lname=person.lname).first()
            if existing_person:
                raise ValueError("Person with this name already exists")

            db.session.add(person)
            db.session.commit()
            return person
        except DBAPIError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")

        
    @staticmethod   
    def read_one(id):
        existing_person = db.session.get(Person, id)

        if not existing_person:
            raise ValueError(f"Person with id {id} not found")
        return existing_person

    @staticmethod
    def update(id, person):
        try:
            existing_person = db.session.get(Person, id)
            
            if not existing_person:
                raise ValueError(f"Person with id {id} not found")
            
            if hasattr(person, 'fname') and person.fname:
                existing_person.fname = person.fname
            if hasattr(person, 'lname') and person.lname:
                existing_person.lname = person.lname

            db.session.commit()
            return existing_person
        except DBAPIError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        
    @staticmethod    
    def remove(id):
        try:
            existing_person = db.session.get(Person, id)

            if not existing_person:
                raise ValueError(f"Person with id {id} not found")
            
            db.session.delete(existing_person)
            db.session.commit()
        except DBAPIError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")