from flask import render_template, redirect, url_for, session
from app import app, db
from programme.models import Programme
from user.models import Users
from programme.forms import CreateProgrammeForm
from slugify import slugify
from user.decorators import login_required


@app.route("/admin/createprogramme/", methods=('GET', 'POST'))
@login_required
def create_programme():

    form = CreateProgrammeForm()

    if form.validate_on_submit():
        slug = slugify(form.title.data)
        user = Users.query.filter_by(username=session["username"]).first()
        user = user.id
        programme = Programme(user, form.title.data, form.overview.data, form.outcome.data, form.course_code.data,
                              form.duration.data, form.location.data, form.date.data, form.period.data, form.time.data,
                              form.fee.data, slug)
        if programme:
            db.session.add(programme)
            db.session.flush()
            db.session.commit()
            return redirect(url_for('admin'))
        else:
            error = "Unable to create programme"
            db.session.rollback()
            return render_template("programme/createprogramme.html", form=form, error=error)
    return render_template("programme/createprogramme.html", action="new", form=form)


@app.route("/admin/programme/update")
@login_required
def updateprogramme():
    programme = Programme.query.order_by(Programme.date.asc()).all()

    return render_template("programme/updateprogramme.html", programme=programme)


@app.route("/admin/programme/update/<slug>", methods=("POST", "GET"))
@login_required
def update(slug):
    programme = Programme.query.filter_by(slug=slug).first_or_404()

    form = CreateProgrammeForm(obj=programme)

    if form.validate_on_submit():
        form.populate_obj(programme)
        db.session.commit()
        return redirect(url_for("updateprogramme"))
    return render_template("programme/createprogramme.html", action="edit", form=form, programme=programme)
