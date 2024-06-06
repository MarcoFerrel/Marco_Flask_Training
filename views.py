from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': "El Paso, Texas",
        'salary': "$80,000"
    },
     {
        'id': 2,
        'title': 'Software Engineer',
        'location': "Austin, Texas",
        'salary': "$120,000"
    },
     {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': "Austin, Texas",
        'salary': "$180,000"
    }
]


@views.route("/")
def home():
    return render_template("index.html", jobs=JOBS)

@views.route("/profile")
def profile():  
    return render_template("profile.html")

@views.route("/jobs")
def get_json():
     return  jsonify(JOBS)

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def  go_to_home():
    return redirect(url_for("views.home"))
