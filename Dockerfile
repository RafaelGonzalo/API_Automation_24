# Imagen con Python 3
FROM python:3

# Mantenedor
LABEL maintainer="rafael.alfaro@jalasoft.com"

# Actualizar el sistema y instalar Java
RUN apt-get update && apt-get install -y default-jre && java -version

# Instalar Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb && \
    dpkg -i allure_2.18.1-1_all.deb && rm allure_2.18.1-1_all.deb

# Copiar el código al directorio /opt/app
COPY . /opt/app
WORKDIR /opt/app

# Instalar la biblioteca/paquete virtualenv y crear un entorno virtual para el framework
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install virtualenv && \
    python3 -m virtualenv env

# Activar el entorno virtual y luego instalar los requisitos y ejecutar los tests
RUN . env/bin/activate && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pylint clickup_api/ --rcfile=.pylintrc && \
    python -m pytest clickup_api/ -v -s --alluredir reports/allure/allure-results --clean-alluredir  && \
    echo "source /opt/app/env/bin/activate" >> ~/.bashrc

# Limpiar el sistema
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean && apt-get autoremove
