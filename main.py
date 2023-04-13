from flask import Flask, render_template, request
import sqlite3
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
    return render_template('loginpage.html', fail_log='')


@app.route('/account')
def account():
    return render_template('accountswitch.html', form_name=act_name)


@app.route('/signin')
def sign():
    return render_template('signinpage.html', fail_sign='')


@app.route('/katalog')
def cat():
    db_file = 'db/sites_base.sqlite'
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    rows = len(cur.execute("SELECT * FROM sites").fetchall())
    titles = cur.execute("SELECT name FROM sites").fetchall()
    type = cur.execute("SELECT type FROM sites").fetchall()
    age = cur.execute("SELECT age FROM sites").fetchall()
    type_age = [type[i][0] + ', ' + age[i][0] for i in range(len(type))]
    links = cur.execute("SELECT link FROM sites").fetchall()
    img = cur.execute("SELECT img FROM sites").fetchall() # width="237" height="151"
    description = []
    for i in titles:
        from parsing_sites import connection
        description.append(connection.pars(i[0]))
    if act_name == 0:
        return render_template('catalog.html', n=rows, game_names=titles, game_types=type_age,
                               game_descriptions=description, game_links=links, game_img=img)
    else:
        return render_template('catalog_acc.html', form_name=act_name, n=rows, game_names=titles, game_types=type_age,
                               game_descriptions=description, game_links=links, game_img=img)


@app.route('/video')
def video():
    db_file = 'db/sites_base.sqlite'
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    rows = len(cur.execute("SELECT * FROM sites WHERE type in ('Видео-уроки')").fetchall())
    titles = cur.execute("SELECT name FROM sites WHERE type in ('Видео-уроки')").fetchall()
    type = cur.execute("SELECT type FROM sites WHERE type in ('Видео-уроки')").fetchall()
    age = cur.execute("SELECT age FROM sites WHERE type in ('Видео-уроки')").fetchall()
    type_age = [type[i][0] + ', ' + age[i][0] for i in range(len(type))]
    links = cur.execute("SELECT link FROM sites WHERE type in ('Видео-уроки')").fetchall()
    img = cur.execute("SELECT img FROM sites WHERE type in ('Видео-уроки')").fetchall()  # width="237" height="151"
    description = []
    for i in titles:
        from parsing_sites import connection
        description.append(connection.pars(i[0]))
    if act_name == 0:
        return render_template('catalog.html', n=rows, game_names=titles, game_types=type_age,
                               game_descriptions=description, game_links=links, game_img=img)
    else:
        return render_template('catalog_acc.html', form_name=act_name, n=rows, game_names=titles, game_types=type_age,
                               game_descriptions=description, game_links=links, game_img=img)


@app.route('/get-text', methods=['GET', 'POST'])
def foo():
    global act_name
    check = ''
    bar = request.form['login']
    bur = request.form['password']
    if len(bar) < 1:
        if len(bur) < 8:
            return render_template('signinpage.html', fail_sign='Пароль и логин слишком короткие')
        else:
            return render_template('signinpage.html', fail_sign="Логин слишком короткий")
    else:
        if len(bur) < 8:
            return render_template('signinpage.html', fail_sign='Пароль слишком короткий')
    from data import db_session
    db_session.global_init("db/users_base.sqlite")
    session = db_session.create_session()
    check = db_session.check_user(bar, bur, session)
    if check == '':
        act_name = db_session.add_user(bar, bur, session) + '  '
        return render_template('hpage_acc.html', form_name=act_name)
    else:
        return render_template('signinpage.html', fail_sign=check)


@app.route('/get-text2', methods=['GET', 'POST'])
def you():
    global act_name
    check = ''
    bar = request.form['login']
    bur = request.form['password']
    from data import db_session
    db_session.global_init("db/users_base.sqlite")
    session = db_session.create_session()
    check = db_session.check_user(bar, bur, session)
    if check == '':
        check = 'Такого пользователя не существует'
        return render_template('loginpage.html', fail_log=check)
    else:
        act_name = bar + '  '
        return render_template('hpage_acc.html', form_name=act_name)


@app.route('/h', methods=['GET', 'POST'])
def h():
    global act_name
    act_name = 0
    return render_template('homepage.html')


@app.route('/s', methods=['GET', 'POST'])
def s():
    global act_name
    act_name = 0
    return render_template('signinpage.html', fail_sign='')


@app.route('/l', methods=['GET', 'POST'])
def lo():
    global act_name
    act_name = 0
    return render_template('loginpage.html', fail_log='')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')