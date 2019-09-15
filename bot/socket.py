import asyncio
import websockets
import json

from chatterbot import ChatBot


chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpus'
)


async def chat_receiver(websocket, path):
    async for message in websocket:
        message = json.loads(message)
        text = message['text']

        chat_response = chatbot.get_response(text).text
        print(chat_response)

        await websocket.send(json.dumps({'response': chat_response}))


async def router(websocket, path):
    if path == '/':
        await chat_receiver(websocket, path)


asyncio.get_event_loop().run_until_complete(websockets.serve(router, '0.0.0.0', 8888))

asyncio.get_event_loop().run_forever()