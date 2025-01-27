from celery import shared_task
import json
from live_scraper.views.scraper import live_data


@shared_task
def process_live_data():
    with open("live_data.json", "w") as file:
        json.dump(live_data, file)
    live_data.clear()
