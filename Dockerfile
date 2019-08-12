FROM python:3

RUN pip3 install pipenv

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pipenv install --dev \
 && pipenv lock --dev -r > requirements.txt \
 && pipenv run python setup.py bdist_wheel
