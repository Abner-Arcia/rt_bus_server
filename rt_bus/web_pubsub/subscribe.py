import asyncio
from azure.messaging.webpubsubservice import build_authentication_token
import websockets

async def connect(url):
    async with websockets.connect(url) as ws:
        print('connected')
        while True:
            print('Message received: ' + await ws.recv())

connection_string = ''
hub_name = ''

token = build_authentication_token(connection_string, hub_name)

try:
    asyncio.get_event_loop().run_until_complete(connect(token['url']))
except KeyboardInterrupt:
    pass