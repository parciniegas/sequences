from fastapi import APIRouter, HTTPException, status
from models import client

client_router = APIRouter(prefix="/client", tags=["Client"])

@client_router.get("/")
async def get_clients():
    return client.get_clients()

@client_router.get("/{client_id}")
async def get_client(client_id: int):
    client_list = client.get_client(client_id)
    if client_list:
        return client_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

@client_router.post("/")
async def create_client(client_data: client.Client):
    client_id = client.create_client(client_data)
    return {"client_id": client_id}

@client_router.put("/{client_id}")
async def update_client(client_id: int, client_data: client.Client):
    client.update_client(client_id, client_data)
    return {"client_id": client_id}

@client_router.delete("/{client_id}")
async def delete_client(client_id: int):
    client.delete_client(client_id)
    return {"client_id": client_id}