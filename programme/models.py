from app import db


class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(256))
    overview = db.Column(db.String())
    outcome = db.Column(db.String())
    course_code = db.Column(db.String(10), unique=True)
    duration = db.Column(db.String(10))
    location = db.Column(db.String(80))
    slug = db.Column(db.String(256), unique=True)
    date = db.Column(db.Date)
    period = db.Column(db.String(80))
    time = db.Column(db.String(10))
    fee = db.Column(db.Integer())
    live = db.Column(db.Boolean)

    def __init__(self, user, title, overview, outcome, course_code, duration, location, date, period, time, fee, slug, live=True):
        self.user = user
        self.title = title
        self.overview = overview
        self.outcome = outcome
        self.course_code = course_code
        self.duration = duration
        self.location = location
        self.date = date
        self.period = period
        self.time = time
        self.fee = fee
        self.slug = slug
        self.live = live

    def __repr__(self):
        return "<Programme %r>" % self.title
