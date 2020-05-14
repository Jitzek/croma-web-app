# Imports #
from flask import Blueprint, render_template

# Configuration
live_api = Blueprint('live_api', __name__)

# Routes #
@live_api.route('/live')
def livepage():
    return render_template('live.html', stream_host="localhost", stream_port=2222)