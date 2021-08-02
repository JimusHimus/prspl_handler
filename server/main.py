import asyncio
import aioconsole as aioconsole
import websockets
from websockets.exceptions import ConnectionClosedError

clients = set()


# when client sent message
def handle_message(message):
    print(f'Got message from client: {message}')


# when client connected
async def handle_client(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            handle_message(message)
    except ConnectionClosedError:
        pass
    finally:
        clients.remove(websocket)


async def notify_clients():
    while True:
        message = await aioconsole.ainput()
        for client in clients:
            await client.send(message)


def start_server():
    server = websockets.serve(handle_client, "localhost", 5656)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().create_task(notify_clients())
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    start_server()
