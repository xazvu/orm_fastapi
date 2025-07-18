import uvicorn
from fastapi import FastAPI

from db.engine import init_db
from __inti__ import router

init_db()

app = FastAPI()
app.include_router(router)

@app.get("/", name='home page')
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

