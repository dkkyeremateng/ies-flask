from app import app
import sqlalchemy


try:
    db_uri = 'postgresql://localhost/'
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute('CREATE DATABASE ' + app.config["BLOG_DATABASE_NAME"])
    print("connected")
except Exception as e:
    print("Database exist")
    print(str(e))
    print(e.__class__)

from app import db

# Add models here
from programme import models
from user import models

db.create_all()
