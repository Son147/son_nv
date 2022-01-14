from flask import (Flask, request, render_template, session, redirect, g,url_for)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1418, debug=True)