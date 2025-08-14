import time
from src.events.image_update import ImageUpdateEvent

def image_handler(event: ImageUpdateEvent):
    print(f"Processing image update event for bucket: {event.bucket}, key: {event.key}")
    time.sleep(60)
    print("Finished processing image update event")