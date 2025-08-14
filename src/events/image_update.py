from pydantic import BaseModel

class ImageUpdateEvent(BaseModel):
    bucket: str
    key: str