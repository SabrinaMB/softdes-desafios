# Documentação de desenvolvedor

## Quick Start
1. Sem docker:
   1. No diretorio "~/.../softdes-desafios/src"
      1. Rode o comando "sudo pip3 install -r requirements.txt"
           * se não funcionar, tente "sudo python3 -m pip install -r "./../requirements.txt""
      2. Rode os seguintes comandos em um terminal:
          * sqlite3 quiz.db ".exit"
          * sudo chmod 777 quiz.db 
          * sudo sqlite3 quiz.db < quiz.sql
      3. Crie um arquivo "users.csv"
          1. Insira seu {nome} e o {tipo} de usuario que você é nesse arquivo, no formato "{nome}, {tipo}"
      4. Rode o comando "sudo python3 adduser.py"
      5. Rode o comando "sudo python3 softdes.py"
2. Com docker:
   1. Na pasta base (softdes-desafios) rode:
      1. docker volume create quiz.db
      2. sudo docker build -t desafios . 
      3. sudo docker run -p 0.0.0.0:8080:80 -v /var/lib/docker/volumes/quiz.db/_data:/src desafios
3. Para rodar os testes de interface:
   1. instale geckodriver
   2. ponha o caminho até ele no PATH
   3. crie uma variável de ambiente com o endereço em que está rodando o seu servidor. 
      1. Ex.: ADDRESS=0.0.0.0:8080
