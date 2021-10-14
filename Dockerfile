FROM python

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN sqlite3 src/quiz.db ".exit"
RUN sqlite3 src/quiz.db < src/quiz.sql
RUN sqlite3 src/quiz.db "UPDATE QUIZ SET expire='2021-12-12' WHERE id=1;"
RUN cat src/quiz.db
RUN python3 src/adduser.py

EXPOSE 8080

ENTRYPOINT python3 src/softdes.py
