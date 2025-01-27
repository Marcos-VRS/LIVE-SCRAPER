import json
from channels.generic.websocket import AsyncWebsocketConsumer


class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            print("Cliente tentou se conectar")
            await self.accept()
        except Exception as e:
            print(f"Erro ao conectar: {e}")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps(data))
