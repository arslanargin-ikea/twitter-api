from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    from config import Config
    from app.models import Tweet
    from flask_migrate import Migrate
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False

    return app

