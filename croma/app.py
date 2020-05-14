#! /usr/bin/python3.7

# Imports #
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
#from db import DB

# Configuration
app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/cromaDB"
#DB.setDB(PyMongo(app))

# Blueprints #
from home import home_api
from live import live_api
from metingen import metingen_api
from about import about_api
from contact import contact_api
from updates import updates_api

app.register_blueprint(home_api)
app.register_blueprint(live_api)
app.register_blueprint(metingen_api)
app.register_blueprint(about_api)
app.register_blueprint(contact_api)
app.register_blueprint(updates_api)

# Routes #
@app.route('/')
def index():
    return redirect("/home")

# Error Code Handling #
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error_page.html', error=500, msg="Internal Server Error")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_page.html', error=404, msg="Page not Found")

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('error_page.html', error=403, msg="Forbidden")
# etc.

# Development Server (localhost:8080)
if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)