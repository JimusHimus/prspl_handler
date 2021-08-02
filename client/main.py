import asyncio
import websockets
from websockets.exceptions import ConnectionClosedError


# when client get message from server
def handle_message(message):
    return 'Handled message ' + message


async def connect():
    uri = "ws://localhost:5656"
    while True:
        async with websockets.connect(uri) as websocket:
            await websocket.send('I\'m ready')
            try:
                while True:
                    message = await websocket.recv()
                    print(f'Got message from server: {message}')
                    handled_message = handle_message(message)
                    await websocket.send(handled_message)
            except ConnectionClosedError:
                pass


def run_client():
    asyncio.get_event_loop().run_until_complete(connect())
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    run_client()
