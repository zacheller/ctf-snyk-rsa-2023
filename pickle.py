import pickle
import base64

from flask import Flask, request

app = Flask(__name__)

@app.route("http://sauerkraut.c.ctf-snyk.io/", methods=["POST"])
def vulnerable():
    data = base64.urlsafe_b64decode(request.form['pickled'])
    pickle.loads(data)
    return '', 204
