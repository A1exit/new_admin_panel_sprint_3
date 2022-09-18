import datetime
import time
import os.path

import elasticsearch
from config import es_dsl, logger
from extract_from_postgre.extract import (check_change, extract_from_psql,
                                          load_last_mod)
from index_schema.load_schema_es import create_index
from load_to_es.load import bulk_data_to_elastic
from tranform.json_operation import (create_data_to_elastic,
                                     create_dataclass_list)
from utils.backoff_function import backoff


@backoff()
def main():
    if os.path.exists('./modify/modify.json'):
        try:
            now = datetime.datetime.now()
            time_to_check = now + datetime.timedelta(minutes=1)
            if time_to_check.strftime("%Y-%m-%d %H:%M:%S") > load_last_mod():
                create_data_to_elastic(
                    create_dataclass_list(
                        check_change()
                    )
                )
                return es.bulk(index='movies', body=bulk_data_to_elastic('data/data_file.json'))
        except ValueError as error:
            logger.error(error)
    else:
        create_index()
        create_data_to_elastic(
            create_dataclass_list(
                extract_from_psql()
            )
        )
        return es.bulk(index='movies', body=bulk_data_to_elastic(
            'data/data_file.json'
        )
                       )


if __name__ == '__main__':
    if not os.path.exists('./data'):
        os.makedirs('./data')

    if not os.path.exists('./modify'):
        os.makedirs('./modify')

    es = elasticsearch.Elasticsearch(es_dsl, request_timeout=300)
    while True:
        main()
        time.sleep(5)
