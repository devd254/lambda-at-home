from pydantic import BaseModel

class MemoUpdateEvent(BaseModel):
    user_id: int
    memo: str