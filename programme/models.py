from app import db


class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(256))
    course_code = db.Column(db.String(10), unique=True)
    duration = db.Column(db.String(10))
    location = db.Column(db.String(80))
    slug = db.Column(db.String(256), unique=True)
    date = db.Column(db.Date)
    time = db.Column(db.String(10))
    fee = db.Column(db.Integer())
    live = db.Column(db.Boolean)

    def __init__(self, title, course_code, duration, location, date, time, fee, slug, live=True):
        self.title = title
        self.course_code = course_code
        self.duration = duration
        self.location = location
        self.date = date
        self.time = time
        self.fee = fee
        self.slug = slug
        self.live = live

    def __repr__(self):
        return "<Programme %r>" % self.title
