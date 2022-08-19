from flask import Flask
from flask import jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Hello World! testing CD!"


@application.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: {name}")
    val = {"value": name}
    return jsonify(val)


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8080, debug=True)
