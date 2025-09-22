import pytest
from app import create_app
from extensions import db as _db
from src.models.person import Person

@pytest.fixture
def app():
    connex_app = create_app("testing")
    with connex_app.app.app_context():
        _db.create_all()
        yield connex_app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def setOnePerson(app):
    with app.app.app_context():
        person = Person(fname="john", lname="doe")
        _db.session.add(person)
        _db.session.commit()
