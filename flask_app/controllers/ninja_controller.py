from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninjas')
def Ninjas():
    all_dojos = Dojo.get_all_dojos()
    print('All Names Here --------->', all_dojos[0].name)
    return render_template ('new_ninja.html', dojos = all_dojos)

@app.route('/ninjas/added', methods = (['POST']))
def addNinja():
    print(f"\n {request.form} \n")
    Ninja.create(request.form)
    return redirect ('/')