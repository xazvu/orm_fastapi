import uvicorn
from fastapi import FastAPI

from db.engine import init_db
from routers.message import router as message_router
from routers.user import router as user_router

init_db()

app = FastAPI()
app.include_router(user_router)
app.include_router(message_router)

@app.get("/", name='home page')
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)

