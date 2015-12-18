from flask_wtf import Form
# from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators, DateField, SubmitField, IntegerField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from wtforms.fields.html5 import EmailField


class CreateProgrammeForm(Form):
    title = StringField("Programme Title", [validators.DataRequired(), validators.Length(max=256)])
    course_code = StringField("Course Code", [validators.DataRequired()])
    duration = StringField("Duration", [validators.DataRequired()])
    location = StringField("Location", [validators.DataRequired()])
    date = DateField("Date", [validators.DataRequired()])
    time = StringField("Time", [validators.DataRequired()])
    fee = IntegerField("Fee", [validators.DataRequired()])
    submit = SubmitField("Create Programme")
