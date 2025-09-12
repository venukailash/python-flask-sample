import connexion
import pathlib

from flask import render_template
from extensions import db, ma
from src.models.person import Person

basedir = pathlib.Path(__file__).parent.resolve()

def create_app(config_name="default"):
    connex_app = connexion.App(__name__, specification_dir=basedir)
    app = connex_app.app

    app.config.from_object(f"config.{config_name.capitalize()}Config")

    db.init_app(app)
    ma.init_app(app)

    connex_app.add_api('swagger.yml')

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    @app.route("/")
    def home():
        people = Person.query.all()
        return render_template("home.html", people=people)

    return connex_app