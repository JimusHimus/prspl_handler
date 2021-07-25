import asyncio
import websockets


async def handle(websocket, path):
    inp = await websocket.recv()
    print(inp)


def start_server():
    server = websockets.serve(handle, "localhost", 5656)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    start_server()
