from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login')
def login():
    return render_template('loginpage.html')


@app.route('/signin')
def sign():
    return render_template('signinpage.html')


''' если пользователь вошел в аккаунт
@app.route('/hpageacc')
def new():
    return render_template('hpage_acc.html')

'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
