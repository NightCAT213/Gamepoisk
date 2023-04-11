from flask import Flask, render_template, request
app = Flask(__name__)

act_name = 0


@app.route('/')
def index():
    global act_name
    if act_name == 0:
        return render_template('homepage.html')
    else:
        return render_template('hpage_acc.html', form_name=act_name)


@app.route('/login')
def login():
    return render_template('loginpage.html')


@app.route('/account')
def login():
    return render_template('loginpage.html')


@app.route('/signin')
def sign():
    return render_template('signinpage.html', fail_sign='')


@app.route('/get-text', methods=['GET', 'POST'])
def foo():
    global act_name
    check = ''
    bar = request.form['login']
    bur = request.form['password']
    from data import db_session
    db_session.global_init("db/users_base.sqlite")
    session = db_session.create_session()
    check = db_session.check_user(bar, bur, session)
    if check == '':
        act_name = db_session.add_user(bar, bur, session) + '  '
        return render_template('hpage_acc.html', form_name=act_name)
    else:
        return render_template('signinpage.html', fail_sign=check)
    print(bar, bur)
    return 'oy'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')