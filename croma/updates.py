# Imports #
from flask import Blueprint, render_template

# Configuration
updates_api = Blueprint('updates_api', __name__)

# Routes #
@updates_api.route('/updates')
def updatespage():
    return render_template('UpdatesPage.html')