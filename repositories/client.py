from models.client import Client


client_list = []

async def get_client(id: int) -> Client:
    for client in client_list:
        if client['id'] == id:
            return client
    return None

async def get_clients() -> list:
    return client_list

async def create_client(client_data: Client) -> Client:
    client_data['id'] = len(client_list) + 1
    client_list.append(client_data)
    return client_data['id']

async def update_client(id: int, client_data: Client):
    client = get_client(id)
    if client:
        client.update(client_data)
        return client
    return None

async def delete_client(id: int) -> Client:
    client = get_client(id)
    if client:
        client_list.remove(client)
        return client
    return None