import json

from tranform.data_class import Movie


def create_dataclass_list(data):
    body = []
    for record in data:
        data_template = Movie(
            id=record[0],
            imdb_rating=record[1],
            genre=record[2],
            title=record[3],
            description=record[4],
            director=record[5],
            actors_names=record[6],
            writers_names=record[7],
            actors=record[8],
            writers=record[9]
        )
        body.append(data_template)
    return body


def create_data_to_elastic(dataclass_list):
    with open('data/data_file.json', 'w') as f:
        body = []
        for row in dataclass_list:
            index_template = {
                "index": {
                    "_index": "movies",
                    "_id": str(
                        row.id)}}
            data_template = {
                "id": str(row.id),
                "imdb_rating": row.imdb_rating,
                "genre": row.genre,
                "title": row.title,
                "description": row.description,
                "director": row.director,
                "actors_names": row.actors_names,
                "writers_names": row.writers_names,
                "actors": row.actors,
                "writers": row.writers,
            }
            body.append(index_template)
            body.append(data_template)
        json.dump(body, f, indent=4)
