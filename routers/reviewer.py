from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.reviewer import Reviewer
from config.database import Session
from service.reviewer import ReviewerService


reviewer_router = APIRouter()

@reviewer_router.get('/reviewers',tags=['reviewers'], response_model=Reviewer, status_code= 200)
def get_actor() ->Reviewer:   
    db = Session()
    result = ReviewerService(db).get_reviewers()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@reviewer_router.post('/reviewers', tags=['reviewers'], status_code=201 , response_model=dict)
def create_actor(reviewer:Reviewer) ->dict:
    db= Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={'message':'reviewer save in data base'})