# importing the os allows you to interact with the
# operating system on the computer.
import os # noqa
import re # noqa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# env.py not visible in github, check filepath exits locally:
# Cannot just impot it directly
if os.path.exists("env.py"):
    import env # noqa

# Create an instance of the Flask object
app = Flask(__name__)
# Specify two app configuration variables
# The secret key securely signs session cookies:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# set the database location
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Create an instance of the SQLAlchemy class,
# Store in db variable, set to instance of our Flask app
# You are binding the instance of SQLAlchemy to the application
#  called taskmanager
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
