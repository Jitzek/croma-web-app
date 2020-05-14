# Imports #
from flask import Blueprint, render_template

# Configuration
home_api = Blueprint('home_api', __name__)

# Routes #
@home_api.route('/home')
def homepage():
    return render_template('HomePage.html')