FROM python:3

RUN pip install --user pipenv

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pipenv install --dev \
 && pipenv lock -r > requirements.txt \
 && pipenv run python setup.py bdist_wheel
