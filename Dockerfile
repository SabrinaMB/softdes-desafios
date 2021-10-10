FROM python

COPY . .


RUN pip install -r requirements.txt

CMD [ "bash", "src/setup_db.sh"]
CMD [ "python3", "src/adduser.py"]

EXPOSE 80
CMD [ "python3", "src/softdes.py"]

