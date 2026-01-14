from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .data import users
app = FastAPI()
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return "root!"

@app.get("/friends")
async def data():
    return users