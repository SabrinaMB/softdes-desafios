FROM python

COPY . .

RUN pip install -r requirements.txt

CMD [ "bash", "src/setup_db.sh"]
CMD [ "python3", "src/adduser.py"]
CMD [ "docker", "volume", "create", "src/quiz.db"]

EXPOSE 8080
CMD [ "python3", "src/softdes.py"]

