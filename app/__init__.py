from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask_bootstrap import Bootstrap


# app config
app = Flask(__name__)
app.config.from_object("config")

# db config
db = SQLAlchemy(app)

# bootstrap config
bootstrap = Bootstrap(app)

# migrate config
migrate = Migrate(app, db)

from ies.views import *
from programme.views import *
from user.views import *
