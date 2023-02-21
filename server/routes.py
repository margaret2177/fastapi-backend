# from fastapi import APIRouter, Body
# from fastapi.encoders import jsonable_encoder
# from server.model import NoteSchema

# router = APIRouter()

# notes = {
#     "1": {
#         "title": "My first note",
#         "content": "This is the first note in my notes application"
#     },
#     "2": {
#         "title": "Uniform circular motion.",
#         "content": "Consider a body moving round a circle of radius r, wit uniform speed v as shown below. The speed everywhere is the same as v but direction changes as it moves round the circle."
#     }
# }


# @router.get("/")
# async def get_notes() -> dict:
#     return {
#         "data": notes
#     }

# @router.get("/{id}")
# async def get_note(id: str) -> dict:
#     if int(id) > len(notes):
#         return {
#             "error": "Invalid note ID"
#         }

#     for note in notes.keys():
#         if note == id:
#             return {
#                 "data": notes[note]
#             }

# @router.post("/note")
# async def add_note(note: NoteSchema = Body(...)) -> dict:
#     # note.id = str(len(notes) + 1)
#     # notes[note.id] = note.dict()

#     return {
#         "message": "Note added successfully"
#     }

from fastapi import APIRouter, Body
from scraper import Scraper

router = APIRouter()
s = Scraper()



@router.get("/")
async def read_root():
    return 'Hello there!'


@router.get("/api/home/")
async def read_home(page:int=1,filter:str='RAS'):
    # print('page',page)
    # print('filter',filter)
   

    return await s.homeThumbnail(page,filter)

@router.get("/api/details/{path}")
async def read_details(path:str):
    
    return await s.itemDetails(path)

@router.get("/api/search/{term}")
async def read_search(term:str,page:int=1):
 
    return await s.searchResult(term,page)