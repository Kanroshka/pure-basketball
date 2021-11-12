import sqlite3


# Проверка на авторизацию.
def check_auth(login, passw):
    con = sqlite3.connect('DataBase/users')
    cur = con.cursor()

    value = cur.execute('''SELECT * FROM users WHERE name = ?;''', (login, )).fetchall()

    if value != [] and value[0][2] == passw:
        return True
    else:
        return False

    cur.close()
    con.close()


# Регистрация пользователя.
def register(login, passw):
    con = sqlite3.connect('DataBase/users')
    cur = con.cursor()

    value = cur.execute('''SELECT * FROM users WHERE name = ?;''', (login, )).fetchall()

    if value != []:
        return False

    elif value == []:
        cur.execute('''INSERT INTO users (name, password) VALUES (?, ?)''', (login, passw))
        con.commit()
        return True

    cur.close()
    con.close()
