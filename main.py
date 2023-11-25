from fastapi import FastAPI
import src.routes.main as Routes

app = FastAPI()

@app.get("/")
async def init():
    return {"Team":"DragonDevs"}
app.include_router(Routes.questions)

