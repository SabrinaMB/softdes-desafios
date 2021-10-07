# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:00:39 2017

@author: rauli
"""
import sqlite3
import hashlib
import numbers
from datetime import datetime
from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth

DBNAME = 'src/quiz.db'


def lambda_handler(event):
    """Testa a função enviada"""
    try:
        def not_equals(first, second):
            if isinstance(first, numbers.Number) and isinstance(second, numbers.Number):
                return abs(first - second) > 1e-3
            return first != second

        ndes = int(event['ndes'])
        code = event['code']
        args = event['args']
        resp = event['resp']
        diag = event['diag']
        exec(code, locals())

        test = []
        for index, arg in enumerate(args):
            if not 'desafio{0}'.format(ndes) in locals():
                return "Nome da função inválido. Usar 'def desafio{0}(...)'".format(ndes)

            if not_equals(eval('desafio{0}(*arg)'.format(ndes)), resp[index]):
                test.append(diag[index])

        return " ".join(test)
    except:
        return "Função inválida."


def convert_data(orig):
    """Converte a data para o formato correto"""
    return orig[8:10] + '/' + orig[5:7] + '/' + orig[0:4] + ' ' + \
           orig[11:13] + ':' + orig[14:16] + ':' + orig[17:]


def get_quizes(user):
    """Pega todos os quizes que estejam na data certa"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ['admin', 'fabioja']:
        cursor.execute("SELECT id, numb from QUIZ")
    else:
        cursor.execute(
            "SELECT id, numb from QUIZ where release < '{0}'"
                .format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = list(cursor.fetchall())
    conn.close()
    return info


def get_user_quiz(user_id, quiz_id):
    """Pega o resultado do quiz"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sent,answer,result from USERQUIZ where "
        "userid = '{0}' and quizid = {1} order by sent desc"
            .format(user_id, quiz_id))
    info = list(cursor.fetchall())
    conn.close()
    return info


def set_user_quiz(user_id, quiz_id, sent, answer, result):
    """Faz o set de um """
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("insert into USERQUIZ(userid,quizid,sent,answer,result) "
                   "values (?,?,?,?,?);", (user_id, quiz_id, sent, answer, result))
    #
    conn.commit()
    conn.close()


def get_quiz(user_id, user):
    """Faz o get de um quiz"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ['admin', 'fabioja']:
        cursor.execute(
            "SELECT id, release, expire, problem, tests, "
            "results, diagnosis, numb from QUIZ where id = {0}".format(user_id))
    else:
        cursor.execute(
            "SELECT id, release, expire, problem, tests, results, "
            "diagnosis, numb from QUIZ where id = {0} and release < '{1}'"
                .format(user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = list(reg for reg in cursor.fetchall())
    conn.close()
    return info


def set_info(pwd, user):
    """Passa as informações sobre o usuário para o banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE USER set pass = ? where user = ?", (pwd, user))
    conn.commit()
    conn.close()


def get_info(user):
    """Pega informações sobre o usuário"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT pass, type from USER where user = '{0}'".format(user))
    print("SELECT pass, type from USER where user = '{0}'".format(user))
    info = [reg[0] for reg in cursor.fetchall()]
    conn.close()
    if len(info) == 0:
        return None
    return info[0]


AUTH = HTTPBasicAuth()

APP = Flask(__name__, static_url_path='')
APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?TX'


@APP.route('/', methods=['GET', 'POST'])
@AUTH.login_required
def main():
    """Função main"""
    msg = ''
    status = 1
    challenges = get_quizes(AUTH.username())
    sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST' and 'ID' in request.args:
        user_id = request.args.get('ID')
        quiz = get_quiz(user_id, AUTH.username())
        if len(quiz) == 0:
            msg = "Boa tentativa, mas não vai dar certo!"
            status = 2
            return render_template('index.html', username=AUTH.username(),
                                   challenges=challenges, p=status, msg=msg)

        quiz = quiz[0]
        if sent > quiz[2]:
            msg = "Sorry... Prazo expirado!"

        file = request.files['code']
        filename = 'src/upload/{0}-{1}.py'.format(AUTH.username(), sent)
        file.save(filename)
        with open(filename, 'r') as file_read:
            answer = file_read.read()

        args = {"ndes": user_id, "code": answer, "args": eval(quiz[4]),
                "resp": eval(quiz[5]), "diag": eval(quiz[6])}
        print(args)
        feedback = lambda_handler(args)

        result = 'Erro'
        if len(feedback) == 0:
            feedback = 'Sem erros.'
            result = 'OK!'

        set_user_quiz(AUTH.username(), user_id, sent, feedback, result)

    if request.method == 'GET':
        if 'ID' in request.args:
            user_id = request.args.get('ID')
        else:
            user_id = 1

    if len(challenges) == 0:
        msg = "Ainda não há desafios! Volte mais tarde."
        status = 2
        return render_template('index.html', username=AUTH.username(),
                               challenges=challenges, p=status, msg=msg)

    quiz = get_quiz(user_id, AUTH.username())

    if len(quiz) == 0:
        msg = "Oops... Desafio invalido!"
        status = 2
        return render_template('index.html', username=AUTH.username(),
                               challenges=challenges, p=status, msg=msg)

    answers = get_user_quiz(AUTH.username(), user_id)

    return render_template('index.html', username=AUTH.username(),
                           challenges=challenges, quiz=quiz[0],
                           e=(sent > quiz[0][2]), answers=answers,
                           p=status, msg=msg, expi=convert_data(quiz[0][2]))


@APP.route('/pass', methods=['GET', 'POST'])
@AUTH.login_required
def change():
    """Mudança de senha"""
    if request.method == 'POST':
        old = request.form['old']
        new = request.form['new']
        repeat = request.form['again']

        status = 1
        msg = ''
        if new != repeat:
            msg = 'As novas senhas nao batem'
            status = 3
        elif get_info(AUTH.username()) != hashlib.md5(old.encode()).hexdigest():
            msg = 'A senha antiga nao confere'
            status = 3
        else:
            set_info(hashlib.md5(new.encode()).hexdigest(), AUTH.username())
            msg = 'Senha alterada com sucesso'
            status = 3
    else:
        msg = ''
        status = 3

    return render_template('index.html', username=AUTH.username(),
                           challenges=get_quizes(AUTH.username()), p=status,
                           msg=msg)


@APP.route('/logout')
def logout():
    """Caminho para logout"""
    return render_template('index.html', p=2, msg="Logout com sucesso"), 401


@AUTH.get_password
def get_password(username):
    """Pega a senha"""
    return get_info(username)


@AUTH.hash_password
def hash_pw(password):
    """Faz o hash da senha"""
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)

