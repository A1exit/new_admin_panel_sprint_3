import logging
import os

from dotenv import load_dotenv

load_dotenv()

"""Конфигурация для доступа к Elasticsearch"""
es_dsl = [{
    'host': os.environ.get('ELASTIC_HOST'),
    'port': int(os.getenv('ELASTIC_PORT')),
    'scheme': os.getenv('ELASTIC_SCHEME')
}]

"""Конфигурация для доступа к Postgresql"""
psg_dsl = {
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'options': '-c search_path=content'
}

"""Конфигурация логов"""
logging.basicConfig(
    filename='ETL.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger()
