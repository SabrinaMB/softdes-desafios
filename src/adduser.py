"""
Adiciona um novo usuário a partir do arquivo users.csv
"""
import sqlite3
import hashlib


def add_user(new_user, pwd, new_user_type):
    """Adiciona novo usuário"""
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('Insert into USER(user,pass,type) values("{0}","{1}","{2}");'
                   .format(new_user, pwd, new_user_type))
    conn.commit()
    conn.close()


with open('users.csv', 'r') as file:
    LINES = file.read().splitlines()

for users in LINES:
    (user, user_type) = users.split(',')
    print(user)
    print(user_type)
    add_user(user, hashlib.md5(user.encode()).hexdigest(), user_type)
