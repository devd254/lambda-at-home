import time
from src.events.memo_update import MemoUpdateEvent

def memo_handler(event: MemoUpdateEvent):
    print(f"Processing memo update event for user: {event.user_id}")
    time.sleep(30)
    print("Finished processing memo update event")