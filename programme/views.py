from flask import render_template, redirect, url_for
from app import app, db
from programme.forms import CreateProgrammeForm
from programme.models import Programme
from slugify import slugify
from user.decorators import login_required


@app.route("/createprogramme/", methods=('GET', 'POST'))
@login_required
def create_programme():

    form = CreateProgrammeForm()

    if form.validate_on_submit():
        slug = slugify(form.title.data)

        programme = Programme(form.title.data, form.course_code.data, form.duration.data,
                              form.location.data, form.date.data, form.time.data, form.fee.data, slug)
        if programme:
            db.session.add(programme)
            db.session.flush()
            db.session.commit()
            return redirect(url_for('training'))
        else:
            db.session.rollback()
            return render_template("programme/createprogramme.html", form=form)
    return render_template("programme/createprogramme.html", form=form)
