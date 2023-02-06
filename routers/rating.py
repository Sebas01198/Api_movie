from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.rating import Rating
from config.database import Session
from service.rating import RatingService


rating_router = APIRouter()

@rating_router.get('/ratings',tags=['ratings'], response_model=Rating, status_code= 200)
def get_actor() ->Rating:   
    db = Session()
    result = RatingService(db).get_ratings()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@rating_router.post('/ratings', tags=['ratings'], status_code=201 , response_model=dict)
def create_actor(rating:Rating) ->dict:
    db= Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={'message':'rating save in data base'})

@rating_router.put('/ratings{id}',tags=['ratings'])
def update_genres(id:int,rating:Rating):
    db =  Session
    result = RatingService(db).update_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    RatingService(db).update_genres(id,rating)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})