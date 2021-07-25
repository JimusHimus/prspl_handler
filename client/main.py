import asyncio
import websockets


async def client():
    uri = "ws://localhost:5656"
    async with websockets.connect(uri) as websocket:
        name = input("Type something")
        await websocket.send(name)


def run_client():
    asyncio.get_event_loop().run_until_complete(client())


if __name__ == '__main__':
    run_client()
