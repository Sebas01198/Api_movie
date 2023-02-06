from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.genres import Genres
from models.genres import Genres as GenresModel
from service.genres import GenresService


genres_router = APIRouter()


@genres_router.get('/genres/{id_movie}/genres/', tags=['genres'],response_model=list[Genres],status_code=200)
def get_genres(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = GenresService(db).get_genres(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.post('/genres', tags=['genres'],response_model=dict,status_code=201)
def create_genres(genres:Genres)->dict:
    db = Session()
    GenresService(db).create_genres(genres)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})

@genres_router.put('/genres{id}',tags=['genres'])
def update_genres(id:int,genres:Genres):
    db =  Session
    result = GenresService(db).update_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    GenresService(db).update_genres(id,genres)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})