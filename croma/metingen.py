# Imports #
from flask import Blueprint, render_template

# Configuration
metingen_api = Blueprint('metingen_api', __name__)

# Routes #
@metingen_api.route('/metingen')
def metingenpage():
    return render_template('MetingenPage.html', stream_host="localhost", stream_port=2222, socket_host="localhost", socket_port=4444)