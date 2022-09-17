from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.schema import List, Optional


class PersonModel(BaseModel):
    id: str
    name: str


class Movie(BaseModel):
    id: UUID
    imdb_rating: Optional[float]
    genre: Optional[List]
    title: str
    description: Optional[str]
    director: Optional[List]
    actors_names: Optional[List]
    writers_names: Optional[List]
    actors: Optional[List]
    writers: Optional[List]

    @validator('imdb_rating')
    def valid_imdb_rating(cls, value):
        if value is None:
            return 0
        return value

    @validator('description')
    def valid_description(cls, value):
        if value is None:
            return ''
        return value

    @validator('director')
    def valid_director(cls, value):
        if value is None:
            return []
        return value

    @validator('actors_names')
    def valid_actors_names(cls, value):
        if value is None:
            return []
        return value

    @validator('writers_names')
    def valid_writers_names(cls, value):
        if value is None:
            return []
        return value

    @validator('actors')
    def valid_actors(cls, value):
        if value is None:
            return []
        return value

    @validator('writers')
    def valid_writers(cls, value):
        if value is None:
            return []
        return value
