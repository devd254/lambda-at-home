from fastapi import FastAPI
from src.dispatcher.registry import EVENT_REGISTRY
from src.dispatcher.scheduler import scheduler
from infra.runner import stop_all_runners
from src.events.image_update import ImageUpdateEvent
from src.events.memo_update import MemoUpdateEvent
import aiofiles

def lifespan():
    # Startup
    yield
    # Teardown
    stop_all_runners()

app = FastAPI(lifespan=lifespan)



@app.post("/dispatch/image")
async def dispatch_image(event: ImageUpdateEvent):
    handler = EVENT_REGISTRY[type(event)]
    await scheduler.schedule_event(handler, event)
    return {"message": "Image event scheduled for execution"}

@app.post("/dispatch/memo")
async def dispatch_memo(event: MemoUpdateEvent):
    handler = EVENT_REGISTRY[type(event)]
    await scheduler.schedule_event(handler, event)
    return {"message": "Memo event scheduled for execution"}

@app.get("/logs")
async def get_logs():
    try:
        async with aiofiles.open("logs.txt", "r") as f:
            logs = await f.readlines()
        return [log.strip() for log in logs]
    except FileNotFoundError:
        return []