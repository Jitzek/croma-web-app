# Imports #
from flask import Blueprint, render_template

# Configuration
about_api = Blueprint('about_api', __name__)

# Routes #
@about_api.route('/about')
def aboutpage():
    return render_template('AboutPage.html')