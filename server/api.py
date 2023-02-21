# from fastapi import FastAPI
# from server.routes import router as NoteRouter

# app = FastAPI()

# @app.get("/", tags=["Root"])
# async def read_root():
#   return { 
#     "message": "Welcome to my notes application, use the /docs route to proceed"
#    }

# app.include_router(NoteRouter, prefix="/note")

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from server.routes import router as Router



# import starlette.responses as responses


origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "https://asianembed.io",
    "https://fastapi-backend-gfs1ok4ks-margaret2177.vercel.app/",
    "http://localhost:3000"

]





app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Router)