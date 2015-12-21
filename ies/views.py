from flask import render_template, request, redirect, url_for
from app import app
from programme.models import Programme, InternationalProgramme
from ies.email import send_email
import pycountry
from datetime import date


countries = list(pycountry.countries)


@app.before_request
def check_date():
    today = date.today()
    programme = Programme.query.order_by(Programme.date.asc()).all()

    for programme in programme:
        if programme.date <= today:
            programme.live = False
        else:
            programme.live = True


@app.route("/")
def index():
    programme = Programme.query.filter_by(live=True).order_by(Programme.date.asc()).limit(4).all()

    inter_programme = InternationalProgramme.query.filter_by(live=True).order_by(InternationalProgramme.date.asc()).limit(4).all()

    return render_template("ies/index.html", programme=programme, inter_programme=inter_programme)


@app.route("/training/")
def training():
    programme = Programme.query.filter_by(live=True).order_by(Programme.date.asc()).all()

    return render_template("ies/training.html", programme=programme)


@app.route("/internationalprogrammes/")
def internationalprogrammes():
    programme = InternationalProgramme.query.filter_by(live=True).order_by(InternationalProgramme.date.asc()).all()

    return render_template("ies/internationalProgrammes.html", programme=programme)


@app.route("/onsite/")
def onsite():
    return render_template("ies/onsite.html")


@app.route("/international/")
def international():
    return render_template("ies/international.html")


@app.route("/requestForProposal/")
def requestforproposal():
    return render_template("ies/requestForProposalForm.html")


@app.route("/trainingRegistration/", methods=("POST", "GET"))
def trainingregistration():
    programme = Programme.query.all()

    if request.method == "POST":

        try:
            send_email("New submission for %s registration!" % request.form['programme'],
                       app.config['MAIL_USERNAME'],
                       request.form['email'],
                       render_template("ies/email.txt", request=request),
                       render_template("ies/email.html", request=request))

            print(request.form['fullName'])
            print(request.form['email'])
            print(request.form['how'])
            return redirect(url_for("index"))
        except Exception as e:
            print(e)
            print(render_template("ies/email.html", request=request))
            error = "Unable to submit form"
            return render_template("ies/trainingRegistration.html", countries=countries, programme=programme, error=error)
    return render_template("ies/trainingRegistration.html", countries=countries, programme=programme)


@app.route("/internationalRegistration/", methods=("POST", "GET"))
def internationalregistration():
    programme = InternationalProgramme.query.all()

    if request.method == "POST":

        try:
            send_email("New submission for %s registration!" % request.form['programme'],
                       app.config['MAIL_USERNAME'],
                       request.form['email'],
                       render_template("ies/email.txt", request=request),
                       render_template("ies/email.html", request=request))

            print(request.form['fullName'])
            print(request.form['email'])
            print(request.form['how'])
            return redirect(url_for("index"))
        except Exception as e:
            print(e)
            print(render_template("ies/email.html", request=request))
            error = "Unable to submit form"
            return render_template("ies/internationalregistration.html", countries=countries, programme=programme, error=error)
    return render_template("ies/internationalregistration.html", countries=countries, programme=programme)


@app.route('/aboutus/')
def aboutus():
    return render_template("ies/aboutUs.html")


@app.route('/programmedetail/<slug>')
def programmedetail(slug):
    programme = Programme.query.filter_by(slug=slug).first_or_404()

    return render_template("ies/seminars/programmedetail.html", programme=programme)


@app.route('/internationalprogrammedetail/<slug>')
def internationalprogrammedetail(slug):
    programme = InternationalProgramme.query.filter_by(slug=slug).first_or_404()

    return render_template("ies/seminars/internationalprogrammedetail.html", programme=programme)


@app.route("/contacts/")
def contact():
    return render_template("ies/contacts.html")


@app.route("/gallery/")
def gallery():
    return render_template("ies/gallery.html")
