# imagen with python 3
FROM python:3

# maintainerlabel
LABEL maintainer="rafael.alfaro@jalasoft.com"

# update system and install java
RUN apt-get update && apt-get install -y default-jre &&  java -version

# install allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb && \
    dpkg -i allure_2.18.1-1_all.deb && rm allure_2.18.1-1_all.deb

# copy the code to /opt/app folder
COPY . /opt/app
WORKDIR /opt/app

# install virtualenv library/package, create virtualenv for the framework
RUN python3 -m pip install --upgrade pip && python3 -m pip install --user virtualenv

RUN python3 -m venv env
# activate virtual environment
RUN . env/bin/activate

# install requirements
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pylint clickup_api/ --rcfile=.pylintrc

RUN python -m pytest clickup_api/ -v -s  --alluredir reports/allure/allure-results --clean-alluredir

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get autoclean && apt-get autoremove