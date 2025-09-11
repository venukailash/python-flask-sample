from src.models.person import Person
from marshmallow_sqlalchemy import fields
from src.schemas.note_schema import NoteSchema
from extensions import db, ma

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships=True
    notes= fields.Nested(NoteSchema,many=True)

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)