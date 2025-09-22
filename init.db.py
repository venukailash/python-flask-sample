from app import create_app
from extensions import db
from src.models.user import User

connex_app = create_app()

with connex_app.app.app_context():
    print("Creating db for first time use...")
    db.create_all()