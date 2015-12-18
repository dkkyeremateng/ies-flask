from app import db
from flask.ext.bcrypt import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    programme = db.relationship("Programme", backref="author", lazy="dynamic")

    def set_password(self, user_password):
        self.password = generate_password_hash(user_password)

    def verify_password(self, user_password):
        return check_password_hash(self.password, user_password)

    @staticmethod
    def register(fullname, email, username, password, is_author, admin):
        user = Users(fullname=fullname, email=email, username=username, is_author=is_author, admin=admin)
        user.set_password(password)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return user

    def __repr__(self):
        return "<Author %r>" % self.username
