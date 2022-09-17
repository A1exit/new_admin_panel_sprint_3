import os

import elasticsearch
from config import es_dsl
from utils.backoff_function import backoff

path = os.path.abspath('schema.json')


@backoff()
def create_index():
    with open(path, 'r') as file:
        data = file.read()
        es = elasticsearch.Elasticsearch(es_dsl, request_timeout=300)
        try:
            es.indices.create(index='movies', body=data)
        except elasticsearch.exceptions.RequestError as ex:
            if ex.error == 'resource_already_exists_exception':
                pass
            else:
                raise ex


create_index()
