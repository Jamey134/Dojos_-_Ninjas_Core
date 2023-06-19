from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('')
def home():