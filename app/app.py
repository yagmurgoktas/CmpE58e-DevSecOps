"""This module provides a simple Flask API endpoint."""

from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    """Return a greeting message."""
    return {"message": "Hello, DevSecOps!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
