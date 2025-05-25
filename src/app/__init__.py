"""
    # This is a simple Flask application that returns a JSON response
    # when the /hello endpoint is accessed.
"""
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    """Return a greeting message."""
    return {"message": "Hello, DevSecOps!"}

@app.route("/bye")
def bye():
    """Return a bye message."""
    return {"message": "Bye, DevSecOps!"}
