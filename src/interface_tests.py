from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


def test_login_success():  # Aluno faz login com sucesso
    try:
        driver.get("http://admin:admin@192.168.15.126/")
        assert True
    except:
        assert False


def test_wrong_password():  # Aluno entra senha incorreta
    try:
        driver.get("http://admin:adm@192.168.15.126/")
        assert False
    except:
        assert True


def test_wrong_answer():  # Aluno envia desafio com resposta incorreta
    try:
        driver.get("http://admin:admin@192.168.15.126/")
        driver.find_element_by_id("resposta").send_keys("adduser.py")
        driver.find_element_by_id("submit").click()
        assert True
    except:
        assert True


def test_right_answer():  # Aluno envia desafio com resposta correta
    try:
        driver.get("http://admin:admin@192.168.15.126/")
        driver.find_element_by_id("resposta").send_keys("desafio.py")
        driver.find_element_by_id("submit").click()
        assert True
    except:
        assert False


driver.close()
