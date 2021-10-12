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
        driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/src/adduser.py")
        driver.find_element_by_id("submit").click()
        assert False
    except:
        assert True
    driver.close()


def test_right_answer():  # Aluno envia desafio com resposta correta
    driver = webdriver.Firefox()
    try:
        driver.get(f"http://admin:admin@{address}/")
        driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/src/desafio.py")
        driver.find_element_by_id("submit").click()
        assert True
    except:
        assert False
    driver.close()
