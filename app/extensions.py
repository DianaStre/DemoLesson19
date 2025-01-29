from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Declaration of DB and Migration
db = SQLAlchemy()
migrate = Migrate()
