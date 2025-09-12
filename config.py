import pathlib
import logging

basedir = pathlib.Path(__file__).parent.resolve()
class DefaultConfig:
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir}/people.db"
        SQLALCHEMY_TRACK_MODIFICATIONS=False

        def __init__(self):
            logging.debug(f'Loading configurations from default config')
                
class TestingConfig(DefaultConfig):
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

        def __init__(self):
            logging.debug(f'Loading configurations from Testing config')