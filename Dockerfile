FROM python:3

COPY ./production /production
COPY ./requirements.txt /


RUN pip install -r /requirements.txt


WORKDIR /production

EXPOSE 5000


CMD ["python", "./web_app/run.py", "&>/dev/null"]
