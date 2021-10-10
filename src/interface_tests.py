from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
print(driver.get("http://admin:admin@192.168.15.126/"))  # Aluno faz login com sucesso
driver.close()
print(driver.get("http://admin:adm@192.168.15.126/"))  # Aluno entra senha incorreta
# driver.find_element_by_id("resposta").send_keys("desafio.py")
# driver.find_element_by_id("submit").click()
driver.close()
