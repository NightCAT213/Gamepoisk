from flask import Flask, render_template, request
from data import db_session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login')
def login():
    return render_template('loginpage.html')


@app.route('/signin')
def sign():
    check = ""
    return render_template('signinpage.html', fail_sign=check)


@app.route('/get-text', methods=['GET', 'POST'])
def foo():
    bar = request.form['login']
    bur = request.form['password']
    check = db_session.check_user(bar, bur)
    if check == '':
        db_session.add_user(bar, bur)
    else:
        return render_template('signinpage.html', fail_sign=check)
    print(bar, bur)


''' если пользователь вошел в аккаунт
@app.route('/hpageacc')
def new():
    return render_template('hpage_acc.html')
    
'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')