import os
from selenium import webdriver

address = os.getenv("ADDRESS")


def test_login_success():  # Aluno faz login com sucesso
    driver = webdriver.Firefox()
    try:
        driver.get(f"http://admin:admin@{address}/")
        assert True
    except:
        assert False
    driver.close()


def test_wrong_password():  # Aluno entra senha incorreta
    driver = webdriver.Firefox()
    try:
        driver.get(f"http://admin:adm@{address}/")
        driver.page_source()
        assert False
    except:
        assert True
    driver.close()


def test_wrong_answer():  # Aluno envia desafio com resposta incorreta
    driver = webdriver.Firefox()
    try:
        driver.get(f"http://admin:admin@{address}/")
        driver.find_element_by_id("resposta").send_keys(os.getcwd() + "/src/adduser.py")
        driver.find_element_by_id("submit").click()
        answers_table = driver.find_element_by_id("answers_table")
        last_answer = answers_table.find_elements_by_id("date")[0]
        assert last_answer.text == "Erro"
    except:
        assert False
    driver.close()


def test_right_answer():  # Aluno envia desafio com resposta correta
    driver = webdriver.Firefox()
    try:
        driver.get(f"http://admin:admin@{address}/")
        driver.find_element_by_id("resposta").send_keys(os.getcwd() + "/src/adduser.py")
        driver.find_element_by_id("submit").click()
        answers_table = driver.find_element_by_id("answers_table")
        last_answer = answers_table.find_elements_by_id("date")[0]
        assert last_answer.text == "OK!"
    except:
        assert False
    driver.close()
