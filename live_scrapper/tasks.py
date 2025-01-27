from celery import shared_task
import json
from views.scrapper import live_data


@shared_task
def process_live_data():
    with open("live_data.json", "w") as file:
        json.dump(live_data, file)
    live_data.clear()
