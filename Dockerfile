FROM python:3.10

WORKDIR /app

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY entrypoint.sh .

COPY 01_etl .

ENTRYPOINT ["sh", "entrypoint.sh"]
