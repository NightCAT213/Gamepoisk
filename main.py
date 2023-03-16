from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/new')
def new():
    return "hello!!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
