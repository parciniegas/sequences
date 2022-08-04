import uvicorn
from fastapi import FastAPI, APIRouter
from services import client

app = FastAPI(
    title="Sequences API", openapi_url="/openapi.json"
)

app.include_router(client.client_router, tags=["Client"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("sequences.main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")