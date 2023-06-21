from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def newDojo():
    # all_dojos = {'name' : 'Detroit'}
    all_dojos = Dojo.get_all_dojos()
    print(" All Dojos -------------->", all_dojos[0].name)
    return render_template ('dojos.html', dojos = all_dojos)

@app.route('/dojos/add', methods=['POST'])
def addDojo():

    Dojo.save(request.form)
    print("\nThis was submitted in the form--------->", request.form, "\n")
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def showDojo(id):

    return render_template('dojo_info.html', dojo_id = Dojo.get_one({'id' : id}), ninjaList=Dojo.get_dojo_with_ninjas({'id' : id}))
