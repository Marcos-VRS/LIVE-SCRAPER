# live_scrapper/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from live_scraper.tasks import scrape_live_data


class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        live_url = data.get("live_url")

        if not live_url:
            await self.send(
                text_data=json.dumps({"error": "URL da live é obrigatória."})
            )
            return

        # Enviar a tarefa para o Celery
        task = scrape_live_data.delay(live_url)

        await self.send(
            text_data=json.dumps({"message": "Scraping iniciado", "task_id": task.id})
        )

    async def disconnect(self, close_code):
        print(f"Cliente desconectado: {close_code}")
