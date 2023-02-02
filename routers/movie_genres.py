from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_genres import MovieGenres
from models.movie_genres import MovieGenres as MovieGenresModel
from service.movie_genres import MovieGenresService


movie_genres_router = APIRouter()


@movie_genres_router.get('/movie_genres', tags=['movie_genres'],response_model=list[MovieGenres],status_code=200)
def get_movie_genres(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieGenresService(db).get_movie_genres(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_genres_router.post('/movie_genres', tags=['movie_genres'],response_model=dict,status_code=201)
def create_genres(genres:MovieGenres)->dict:
    db = Session()
    MovieGenresService(db).create_movie_genres(genres)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})

@movie_genres_router.put('/movie_genres{id}',tags=['movie_genres'])
def update_movie_genres(id:int,movie_genres:MovieGenres):
    db =  Session
    result = MovieGenresService(db).update_movie_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieGenresService(db).update_movie_genres(id,MovieGenres)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})
