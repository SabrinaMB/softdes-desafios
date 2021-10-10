# Documentação de desenvolvedor

## Quick Start
1. Sem docker:
   1. No diretorio "~/.../softdes-desafios/src"
       1. Rode o comando "./setup_db.sh" em um terminal
           * se não funcionar, tente "bash ./setup_db.sh"
       2. Rode o comando "sudo pip3 install -r requirements.txt"
           * se não funcionar, tente "sudo python3 -m pip install -r "./../requirements.txt""
       3. Crie um arquivo "users.csv"
           1. Insira seu {nome} e o {tipo} de usuario que você é nesse arquivo, no formato "{nome}, {tipo}"
       4. Rode o comando "python3 adduser.py"
       5. Rode o comando "sudo python3 softdes.py"
2. Com docker:
   1. docker build - < Dockerfile
   2. docker run -p 0.0.0.0:8080:80 softdes
