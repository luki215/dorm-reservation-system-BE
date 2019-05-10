# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7
WORKDIR /dorm-be
RUN pip install --no-cache ptvsd
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache -r requirements.txt