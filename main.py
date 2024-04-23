from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ['buy food', 'do hw']
class count(BaseModel):
    tracker: int = 0
likeCount = count()

# class Item extends/implements BaseModel
class Item(BaseModel):
    number: int

class Element(BaseModel):
    number: int

@app.get('/items')
async def get_items():
    return likeCount

@app.post('/add')
async def add_item():
    likeCount.tracker += 1
    return {'message': 'you received <3'}


@app.delete('/remove')
async def remove_item():
        likeCount.tracker -= 1
        return {'message': 'You lost a like, its ok, you will get another'}
