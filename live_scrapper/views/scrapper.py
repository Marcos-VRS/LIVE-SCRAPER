from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent, CommentEvent, GiftEvent
import json

# Inicializar o cliente
client = TikTokLiveClient(unique_id="@username_tiktok")

# Variável para armazenar dados
live_data = []


@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    live_data.append(
        {
            "event": "like",
            "username": event.user.nickname,
            "likes": event.total_likes,
            "timestamp": event.timestamp,
        }
    )


@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    live_data.append(
        {
            "event": "comment",
            "username": event.user.nickname,
            "comment": event.comment,
            "timestamp": event.timestamp,
        }
    )


@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    live_data.append(
        {
            "event": "gift",
            "username": event.user.nickname,
            "gift": event.gift.name,
            "amount": event.gift.amount,
            "timestamp": event.timestamp,
        }
    )


# Função para iniciar o cliente
def start_tiktok_client():
    client.run()
