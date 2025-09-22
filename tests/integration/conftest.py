import pytest
from app import create_app
from extensions import db as _db
from src.models.user import User

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
def setOneUser(app):
    with app.app.app_context():
        user = User(email="v@b.com", first_name="john", last_name="doe")
        _db.session.add(user)
        _db.session.commit()
