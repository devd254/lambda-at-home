from handlers.image import image_handler
from handlers.memo import memo_handler
from src.events.image_update import ImageUpdateEvent
from src.events.memo_update import MemoUpdateEvent

EVENT_REGISTRY = {
    ImageUpdateEvent: image_handler,
    MemoUpdateEvent: memo_handler,
}