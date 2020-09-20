FROM python:3.8

WORKDIR /usr/src/forum_django

COPY . /usr/src/forum_django
COPY ./requirements.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt


EXPOSE 8000
CMD ["export", "$(cat", ".env)"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]