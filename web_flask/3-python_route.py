#!/usr/bin/python3
"""
    script that starts a Flask web application,
    must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_world():
    """ that display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ that display HBNB """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ display C  followed by the value of the text variable """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """ display Python , followed by the value of the text variable """
    return ("Python {}".format(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
