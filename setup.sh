#!/bin/bash

sqlite3 src/quiz.db ".exit"
sqlite3 src/quiz.db < src/quiz.sql
sqlite3 src/quiz.db "UPDATE QUIZ SET expire='2021-12-12' WHERE id=1;"
python3 src/adduser.py
