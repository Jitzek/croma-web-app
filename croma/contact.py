# Imports #
from flask import Blueprint, render_template

# Configuration
contact_api = Blueprint('contact_api', __name__)

# Routes #
@contact_api.route('/contact')
def contactpage():
    return render_template('ContactPage.html')