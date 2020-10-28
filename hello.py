# Flask demo program

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!'


@app.route('/hello')
def greeting():
    return 'Welcome to Flask!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
