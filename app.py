import connexion
import pathlib

from extensions import db, ma

basedir = pathlib.Path(__file__).parent.resolve()

def create_app(config_name="default"):
    connex_app = connexion.App(__name__, specification_dir=basedir)
    app = connex_app.app

    app.config.from_object(f"config.{config_name.capitalize()}Config")

    db.init_app(app)
    ma.init_app(app)

    connex_app.add_api('swagger.yml')

    return connex_app