import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import src.routes.main as Routes
load_dotenv()

app = FastAPI()

origins = os.environ.get("ORIGINS").split(",")

print(origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def init():
    return {"team":os.environ.get("TEAM")}
app.include_router(Routes.questions)

