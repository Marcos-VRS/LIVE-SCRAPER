from django.core.management.base import BaseCommand
from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent, CommentEvent, GiftEvent
from live_scraper.models import LiveInfo


class Command(BaseCommand):
    help = "Start TikTok Live Scraper"

    def handle(self, *args, **kwargs):
        client = TikTokLiveClient(unique_id="@username_tiktok")

        @client.on(LikeEvent)
        async def on_like(event: LikeEvent):
            LiveInfo.objects.create(
                data={
                    "event": "like",
                    "username": event.user.nickname,
                    "likes": event.total_likes,
                    "timestamp": event.timestamp,
                }
            )

        @client.on(CommentEvent)
        async def on_comment(event: CommentEvent):
            LiveInfo.objects.create(
                data={
                    "event": "comment",
                    "username": event.user.nickname,
                    "comment": event.comment,
                    "timestamp": event.timestamp,
                }
            )

        @client.on(GiftEvent)
        async def on_gift(event: GiftEvent):
            LiveInfo.objects.create(
                data={
                    "event": "gift",
                    "username": event.user.nickname,
                    "gift": event.gift.name,
                    "amount": event.gift.amount,
                    "timestamp": event.timestamp,
                }
            )

        self.stdout.write("Starting TikTok Live Scraper...")
        client.run()
