from flask import Flask
from app.items import items
from app.main import main
from app.extensions import db, migrate



def create_app():
    app = Flask(__name__)

# Configuring DB
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialization of DB and Migration

    db.init_app(app) # always refers to app.db as configured above
    migrate.init_app(app, db)

# Template creation for our app.db

    class Event(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        description = db.Column(db.String(80), nullable=True)
        date = db.Column(db.String(80), nullable=False)
        time = db.Column(db.String(80), nullable=False)



# Initializing blueprint
    app.register_blueprint(main)
    app.register_blueprint(items)


    return app



