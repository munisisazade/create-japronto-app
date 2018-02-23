FROM python:3.5

ENV APP_ROOT /code

ADD requirements.txt /requirements.txt

RUN pyvenv /venv \
    && /venv/bin/pip install -U pip \
    && /venv/bin/pip install -r requirements.txt


RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

EXPOSE 8050

CMD ["/venv/bin/python", "/code/app.py"]
