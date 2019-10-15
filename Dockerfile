# Container base: python 3.7 Alpine Linux
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /code

# Define o diretório de trabalho
WORKDIR /code

# "Copia" arquivo requirements.txt para o diretorio code
ADD requirements.txt /code/

# Executa o pip
RUN pip install -r requirements.txt

# "Copia" os arquivos locais para o diretorio code no container 
ADD . /code/

# Faz todas as migrações
RUN python manage.py makemigrations
RUN python manage.py migrate
