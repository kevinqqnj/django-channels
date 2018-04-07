FROM python:3

ENV PYTHONUNBUFFERED 1
# 防止中文乱码
ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt
